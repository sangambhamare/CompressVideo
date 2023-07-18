import streamlit as st
import moviepy.editor as mp

def main():
    st.title("Video Compressor")
    st.write("Upload a large video and set the desired compression settings below:")

    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.write("Video Preview:")
        st.video(uploaded_file)

        compression_factor = st.slider("Compression Factor", min_value=0.1, max_value=1.0, step=0.1, value=0.5)

        if st.button("Compress"):
            compressed_video = compress_video(uploaded_file, compression_factor)
            st.write("Download Compressed Video:")
            st.download_button(label="Download", data=compressed_video, file_name="compressed_video.mp4")

def compress_video(video_file, compression_factor):
    video = mp.VideoFileClip(video_file)
    compressed_video = video.resize(compression_factor)
    compressed_filename = "compressed_video.mp4"
    compressed_video.write_videofile(compressed_filename, codec="libx264")
    return compressed_filename

if __name__ == "__main__":
    main()

