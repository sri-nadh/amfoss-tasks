## Sir Perceval’s quest

This was a quiet interesting task...  i learned more about python and json. <br>

I also  got to know that api only returns 30 repo at a time.<br>

So to overcome that i tried to use 
```
?page='+str(page)
```
in the loop <br>
so that i would get atmost 30 repo/page and what i did to stop the loop was if the len(repo) becomes zero, the loop will be terminated.<br>
Then i appended the reponames to a list and after exiting the lopp , i used an another loop to get commits using perceval. 

