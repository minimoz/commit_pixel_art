# commit_pixel_art

Simply draw stuff on your github timeline based on the 5 colors github offers.

## How to use
Firstly set the day when you want to start your pixel art by setting the `days` value in the `commit_pixel_art.py` file.

For example :

`days = 7` will start the drawing 7 seven days before today.

⚠️ You should make it start a Sunday ⚠️

Don't worry, if you made a mistake in the drawing or in the date juste use a git reset : `git reset --hard origin/<branch>` (where `<branch>` is your current branch)

<br />

Then draw your 7x7 stuff in the same file.

<br />

![Alt text](./github_graphic_chart.png?raw=true "Github Graphic Chart")

From left to right colors values are 0, 1, 2, 3, 4.

<br /><br />

For example :

```
pixelArt = [[0, 0, 2, 2, 2, 0, 0],
            [0, 2, 2, 2, 2, 2, 0],
            [2, 0, 4, 2, 0, 4, 2],
            [2, 0, 4, 2, 0, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 0, 2, 0, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0]]
```
Will draw :

![Alt text](./space_invader.png?raw=true "Space Invader")

<br /><br />

Finally execute the script :

`python commit_pixel_art.py`

And then push :

`git push`

<br />

Enjoy 😜
