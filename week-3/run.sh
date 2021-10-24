if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
   python3 main.py bfs 0,8,7,6,5,4,3,2,1
   python3 main.py dfs 0,8,7,6,5,4,3,2,1

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    python main.py bfs 0,8,7,6,5,4,3,2,1
   python3 main.py dfs 0,8,7,6,5,4,3,2,1

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    python main.py bfs 0,8,7,6,5,4,3,2,1
   python3 main.py dfs 0,8,7,6,5,4,3,2,1

fi