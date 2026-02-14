# Universal Video Downloader

> A sleek, modern desktop application for downloading videos and extracting audio from your favorite platforms.

![Screenshot](screenshot.png)

## About

**Universal Video Downloader** is a user-friendly desktop application built with PyQt6 that allows you to download videos and extract audio from various online platforms. Powered by `yt-dlp`, it supports YouTube, TikTok, Instagram, and many other video hosting services.

The application features an intuitive graphical interface that simplifies the download process while providing advanced options for power users.

## Features

✨ **Core Functionality**
- 🎬 Download videos in multiple formats and resolutions
- 🎵 Extract audio with various codec options (MP3, M4A, FLAC, OPUS, WAV)
- ⚙️ Fine-grained quality control (resolution, FPS, bitrate)
- 📝 Automatic subtitle downloading and embedding

🔧 **Advanced Options**
- 🔐 Browser cookie integration (Chrome, Edge, Firefox, Opera) for age-restricted content
- 🎬 FFmpeg postprocessing for metadata and thumbnail embedding
- 🔄 Network resilience with automatic retry and parallel fragment downloads
- 📊 Real-time progress tracking with download speed and size info
- 💾 Disk space monitoring and custom download folder selection

🎨 **User Experience**
- Dark, modern UI with responsive design
- One-click folder access to downloaded files
- System info display (FFmpeg status, yt-dlp version)
- Smooth format/quality selection with dynamic filtering

## How to Use

### 🚀 Quick Start

1. **Download** the latest release from the [Releases](../../releases) page
2. **Extract** the `.exe` file to your preferred location
3. **Run** the application - no installation needed
4. **Paste** a video URL into the input field
5. **Click** "Fetch" to load video information
6. **Adjust** your preferences (format, quality, subtitles, etc.)
7. **Click** "DOWNLOAD" and enjoy

### 📋 Step-by-Step

| Step | Action |
|------|--------|
| 1 | Paste a video link from any supported platform |
| 2 | Click "Fetch" to retrieve available formats |
| 3 | Choose between **Video** or **Audio** mode |
| 4 | Select desired **Format** and **Quality** |
| 5 | Optional: Enable subtitles and browser cookies |
| 6 | Click "DOWNLOAD" to start |

### ⚙️ Settings Explained

- **Type**: Choose between downloading video or extracting audio only
- **Format**: Select video container/codec or audio codec
- **FPS**: Preferred framerate (if unavailable, best alternative is auto-selected)
- **Quality**: Resolution (video) or bitrate (audio)
- **Subtitles**: Download and embed subtitles if available
- **Cookies**: Borrow browser cookies for accessing restricted content

## ⚠️ Signature Warning

This application is **not code-signed**. When you download and run the `.exe` file, Windows may display security warnings such as:

```
Windows Defender SmartScreen has stopped an unrecognized app from starting
```

or

```
This app can't be opened
```

**This is normal.** Code signing certificates are expensive and required for enterprise distributions. To bypass this warning:

1. Click **"More info"** on the warning dialog
2. Click **"Run anyway"** at the bottom
3. The application will launch normally

The source code is publicly available on GitHub for your review and verification. You can also compile it yourself using the provided `uvd.spec` file with PyInstaller if you prefer.

## 📋 System Requirements

- **Windows** 7 or newer (x64)
- **FFmpeg** (optional but recommended for best results)
  - Bundled in the portable package, or
  - Available via system PATH, or
  - Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use for personal and commercial purposes
- ✅ Modify and distribute
- ✅ Include in other projects

With the condition of:
- 📋 Including the original license and copyright notice

---

## 🙏 Credits

Built with:
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - GUI Framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video Downloader
- [FFmpeg](https://ffmpeg.org/) - Media Processor

## 🐛 Issues & Feedback

Found a bug or have a suggestion? Please [open an issue](../../issues) on GitHub!

---

**Happy downloading! 🎉**
