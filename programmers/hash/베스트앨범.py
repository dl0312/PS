genres = ["classic", "classic", "pop", "classic", "classic", "pop", "rock"]
plays = [500, 500, 600, 150, 800, 2500, 3000]

def solution(genres, plays):
    genres_dict = dict()
    genres_total = dict()
    for idx in range(len(plays)):
        genre = genres[idx]
        play = plays[idx]
        if genre in genres_dict.keys():
            genres_dict[genre].append([idx, play])
            genres_total[genre] += play;
        else:
            genres_dict[genre] = [[idx, play]]
            genres_total[genre] = play

    genres_total = sorted(genres_total.items(), key=lambda x: x[1], reverse=True)
    for genre_dict_value in genres_dict.values():
        genre_dict_value.sort(key=lambda x: x[1], reverse=True)
    print(genres_dict)
    print(genres_total)
    total_cnt = 0
    best_album = []
    for genre_info in genres_total:
        genre = genre_info[0]
        for song_cnt in range(2):
            if song_cnt == len(genres_dict[genre]):
                break
            best_album.append(genres_dict[genre][song_cnt][0])
            total_cnt += 1
    return best_album


print(solution(genres, plays))
print("hello")
