from TikTokApi import TikTokApi

api = TikTokApi()

for video in api.trending.videos():
    print(video.author.username)
    # print(video.id)
    # print(video.desc)
    # print(video.author.nickname)
    # print(video.stats.diggCount)
    # print(video.stats.shareCount)
    # print(video.stats.commentCount)
    # print(video.stats.playCount)
    # print(video.createTime)
    # print(video.url)
    # print(video.videoUrl)
    # print(video.music.title)
    # print(video.music.author)
    # print(video.music.album)
    # print(video.music.coverUrl)
    # print(video.music.playUrl)
    # print(video.music.lyric)
    # print(video.music.id)
    # print(video.music.duration)
    # print(video.music.albumId)
    # print(video.music.artistId)
    # print(video.music.artistName)
    # print(video.music.albumName)
    # print(video.music.albumId)
    # print(video.music.artistId)
    # print location of video
    # print(video.location)

    
