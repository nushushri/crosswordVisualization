# crosswordVisualization
My friend and I used to text our NYT mini crossword times to each other every day from May 2021 through January 2022. I decided to collect this data and visualize it. 

I first downloaded our Facebook Messenger conversations as a JSON object, and used regex to extract our times (we used to send our data as as two times separated by a comma, with a colon if the time exceeded 59 seconds [ex. "1:00, 30"]). After that, I used SQLite3 to copy our data into a database table. I created a csv file from the data, and then copied this csv file into the online editor for p5.js (the index.html and style.css files were provided through the editor). In the editor, I created the code to draw two figures consisting of ellipses that vary in color and width/height. 

The color of the ellipses is based on the month. The width of the ellipses represents our time on the mini crossword, and the height of the ellipses represents our time on the mini archive crossword. 

The "mytimes.png" shows my figure that was output based on my data. The csv file also has my data. The recording.mov file shows a video of both figures for my friend and me.

The regex was able to extract about 187 days worth of data--not bad considering that there were ~240 days between May 6 and January 21 (when we played) and we skipped playing once in a while. A few trends that I noticed was that my friend's times were more consistent than mine (my ellipses were varied in width/height) and her average times seemed to be smaller (smaller width/height). I also noticed that there wasn't a lot of improvement over time for either of us.
