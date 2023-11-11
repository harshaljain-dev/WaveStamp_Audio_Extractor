from flask import Flask, render_template, request, redirect
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

app = Flask(__name__)

def add_watermark(input_file, output_file, watermark_text):
    try:
        video = VideoFileClip(input_file)
        print("Video duration:", video.duration)

        # Create TextClip for watermark
        txt_clip = (TextClip(watermark_text, fontsize=50, color='white', bg_color='transparent')
                    .set_duration(video.duration)
                    .set_position(('right', 'bottom'))
                    .set_start(0))

        # Composite the video with the watermark
        watermarked_clip = CompositeVideoClip([video, txt_clip])

        # Write the final video with the watermark
        watermarked_clip.write_videofile(output_file, codec='libx264', threads=4, audio_codec='aac')
    except Exception as e:
        print("Error:", str(e))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/extract', methods=['POST'])
def extract():
    if 'video' not in request.files:
        return redirect(request.url)

    video_file = request.files['video']

    if video_file.filename == '':
        return redirect(request.url)

    video_filename = f'uploads/{video_file.filename}'
    audio_filename = f'uploads/{video_file.filename.replace(".mp4", ".mp3")}'
    watermarked_filename = f'uploads/{video_file.filename.replace(".mp4", "_wm.mp4")}'

    # Save the uploaded video
    video_file.save(video_filename)

    # Extract audio from the video
    video = VideoFileClip(video_filename)
    audio = video.audio
    audio.write_audiofile(audio_filename)

    # Add watermark to the video
    watermark_text = "Your Watermark Text"
    add_watermark(video_filename, watermarked_filename, watermark_text)

    return f'Audio extracted as {audio_filename} and video with watermark saved as {watermarked_filename}'


if __name__ == '__main__':
    app.run(debug=True)
