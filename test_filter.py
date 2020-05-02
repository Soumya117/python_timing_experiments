import time
from typing import List, Dict


musicList: List[Dict[str, str]] = [
    {'Taylor': 'Style', 'Breaking Benjamin': 'So cold', 'Avril': 'Hot'},
    {'Taylor': 'Delicate', 'Breaking Benjamin': 'So cold'},
    {'Taylor': 'Red', 'Justin Beiber': 'Sorry'},
    {'Dua Lipa': 'Levitate', 'Avril': 'Hot'},
    {'Avril': 'Complicated'}
]

musicFilter = ['Taylor', 'Avril']

# experiment 1 is to filter on the basis of if statement

if_time = time.time()
filterMusicIf = []

for music in musicList:
    filterMusicIf.append(
        {
            artist: song for artist, song in music.items()
            if artist in musicFilter
        }
    )
print('time: %s', time.time() - if_time)
print('len(filterMusicIf: ', len(filterMusicIf))
print(filterMusicIf)

# experiment 2 is to use inbuilt filter
filter_time = time.time()
filterMusicFilter = []

for music in musicList:
    filterMusicFilter.append(
        dict(
        filter(
            lambda item: item[0] in musicFilter,
            music.items(),
        )
        )
    )

print('filter time: %s', time.time() - filter_time)
print('len(filterMusicFilter): ', len(filterMusicFilter))
print(filterMusicFilter)
