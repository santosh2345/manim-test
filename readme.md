# Manim Animation Projects 🎬

This repository contains two stunning Manim animation projects that demonstrate the power of mathematical animation programming.

## 📋 Projects Included

### 1. SANTOSH Name Animation
A beautiful animated sequence featuring the name "SANTOSH" with multiple visual effects including:
- Letter-by-letter writing animation
- Rainbow color gradients
- Scaling and rotation effects
- Movement patterns
- Glowing effects and fade transitions

### 2. Client-Server Architecture Animation
A comprehensive visualization of modern distributed system architecture featuring:
- **Client Layer**: Mobile, Desktop, Browser clients
- **Load Balancer**: Request distribution system
- **Web Servers**: Multiple server instances
- **Application Servers**: Backend processing layer
- **Cache Layer**: Redis/Memcached with hit/miss scenarios
- **Database Cluster**: Primary database with read replicas
- **CDN Nodes**: Global content delivery network
- **Auto-scaling**: Dynamic server provisioning
- **Real-time Data Flow**: Animated request/response cycles

## 🛠️ Prerequisites

### Required Software
- **Python 3.8+** (Download from [python.org](https://python.org/downloads/))
- **FFmpeg** (for video rendering)
- **Manim Community Edition**

## 🚀 Installation Guide

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd <repository-name>
```

### Step 2: Install Python Dependencies
```bash
pip install manim
```

### Step 3: Install FFmpeg

#### Windows (Recommended - Using Chocolatey)
1. Install Chocolatey from [chocolatey.org](https://chocolatey.org/install)
2. Open Command Prompt as Administrator:
```bash
choco install ffmpeg
```

#### Windows (Manual Installation)
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your system PATH

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### Step 4: Verify Installation
```bash
python --version
manim --version
ffmpeg -version
```

## 🎥 Running the Animations

### SANTOSH Name Animation
```bash
# Low quality (fast rendering)
manim -pql main.py SantoshAnimation

# Medium quality
manim -pqm main.py SantoshAnimation

# High quality (best output)
manim -pqh main.py SantoshAnimation
```

### Client-Server Architecture Animation
```bash
# Low quality (fast rendering)
manim -pql client-server.py ClientServerArchitecture

# Medium quality
manim -pqm client-server.py ClientServerArchitecture

# High quality (best output)
manim -pqh client-server.py ClientServerArchitecture
```

## 📁 Output Files

After rendering, your videos will be saved in:
```
media/videos/[script-name]/[quality]/[ClassName].mp4
```

**Examples:**
- `media/videos/santosh_animation/480p15/SantoshAnimation.mp4`
- `media/videos/client_server_architecture/480p15/ClientServerArchitecture.mp4`

## ⚙️ Command Line Options

| Flag | Description |
|------|-------------|
| `-p` | Preview video after rendering |
| `-q` | Quality settings (`l`=low, `m`=medium, `h`=high) |
| `-s` | Show last frame instead of video |
| `-a` | Render all scenes in file |
| `--format` | Output format (mp4, gif, png) |

### Example Commands
```bash
# Render without preview
manim -ql santosh_animation.py SantoshAnimation

# Render as GIF
manim -pql --format=gif santosh_animation.py SantoshAnimation

# Render last frame as PNG
manim -s santosh_animation.py SantoshAnimation
```

## 🎨 Animation Features

### SANTOSH Animation (Duration: ~20 seconds)
- ✅ Text writing animation
- ✅ Color gradient transitions
- ✅ Scale and rotation effects
- ✅ Movement patterns
- ✅ Circle creation around text
- ✅ Group rotation effects
- ✅ Glowing stroke effects
- ✅ Smooth fade transitions

### Client-Server Architecture (Duration: ~90 seconds)
- ✅ Progressive component introduction
- ✅ Real-time data flow visualization
- ✅ Load balancing demonstration
- ✅ Cache hit/miss scenarios
- ✅ Auto-scaling simulation
- ✅ Database replication arrows
- ✅ CDN distribution network
- ✅ Performance metrics display
- ✅ System benefits overview

## 🐛 Troubleshooting

### Common Issues and Solutions

#### "FFmpeg not found"
```bash
# Windows: Restart command prompt and verify PATH
ffmpeg -version

# If still not working, reinstall FFmpeg and check PATH
```

#### "Module 'manim' not found"
```bash
pip install --upgrade manim
```

#### "Permission denied" (Windows)
```bash
# Run Command Prompt as Administrator
```

#### Slow rendering
```bash
# Use low quality for testing
manim -pql [script.py] [ClassName]

# Use medium quality for good balance
manim -pqm [script.py] [ClassName]
```

#### Out of memory errors
```bash
# Close other applications
# Use lower quality settings
# Restart your computer
```

## 🎯 Expected Results

### SANTOSH Animation Output
- **File size**: ~2-5 MB (depending on quality)
- **Duration**: 20 seconds
- **Resolution**: 854x480 (low), 1280x720 (medium), 1920x1080 (high)
- **Features**: Colorful text effects with smooth animations

### Client-Server Architecture Output
- **File size**: ~8-15 MB (depending on quality)
- **Duration**: 90 seconds
- **Resolution**: 854x480 (low), 1280x720 (medium), 1920x1080 (high)
- **Features**: Professional system architecture visualization

## 💡 Tips for Best Results

1. **Start with low quality** (`-pql`) for testing
2. **Use high quality** (`-pqh`) for final output
3. **Close unnecessary applications** during rendering
4. **Ensure stable internet** (for dependency downloads)
5. **Check file paths** - avoid spaces in folder names

## 🤝 Contributing

Feel free to:
- Add new animation effects
- Improve existing animations
- Fix bugs or optimize performance
- Create new architectural components
- Submit pull requests

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🆘 Support

If you encounter any issues:

1. **Check Prerequisites**: Ensure Python, Manim, and FFmpeg are properly installed
2. **Verify Commands**: Double-check the command syntax
3. **Check Output**: Look for error messages in the console
4. **File Issues**: Create a GitHub issue with error details

## 🎓 Learning Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Tutorial Videos](https://www.youtube.com/results?search_query=manim+tutorial)
- [Python Installation Guide](https://docs.python.org/3/using/index.html)

---

**Happy Animating! 🎬✨**

*Created with ❤️ using Manim Community Edition*