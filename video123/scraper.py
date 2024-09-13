import subprocess
import os


def download_video(url):

    # 定义 yt-dlp 命令，包含代理设置（如果需要）
    yt_dlp_command = [
        'yt-dlp',
        '--proxy', 'http://127.0.0.1:7890',  # 添加代理设置
        url
    ]
    # 获取当前脚本文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前目录的父目录
    parent_dir = os.path.dirname(current_dir)

    # 构建downloads目录的路径，使其位于当前目录的上一级
    download_dir = os.path.join(parent_dir, 'downloads')

    # 创建downloads目录，如果它不存在
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    # 尝试使用yt-dlp下载视频
    #yt_dlp_command = ['yt-dlp', url]
    yt_dlp_command = ['yt-dlp', '-o', os.path.join(download_dir, '%(title)s.%(ext)s'), url]
    try:
        result = subprocess.run(yt_dlp_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        if result.stderr:
            return f"Error with yt-dlp: {result.stderr}"
        return f'下载成功 : )'
    except subprocess.CalledProcessError as e:
        # yt-dlp下载失败，尝试使用youtube-dl
        print('yt-dlp下载失败，尝试使用youtube-dl...')
        youtube_dl_command = ['youtube-dl', url]
        try:
            result = subprocess.run(youtube_dl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
            if result.stderr:
                return f"Error with youtube-dl: {result.stderr}"
            return f'下载成功!'
        except subprocess.CalledProcessError as e:
            return f'下载失败: {e.stderr}'
    except Exception as e:  # 捕获其他所有异常
        return f'未知错误: {str(e)}'
