---
layout: default
---

[< Home](./)

# **Leaderboard**

|  Rank  | **Team Name**         | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
| #**1** |                       |            |            |
| #**2** |                       |            |            |
| #**3** |                       |            |            |
| #**4** |                       |            |            |
| #**5** |                       |            |            |
| #**6** |                       |            |            |
| #**7** |                       |            |            |
| #**8** |                       |            |            |

## Penalty Log

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|
|        |           |         |                       |

[< Home](./)

```js script
    // Define a function to execute the script
        function executePythonScript() {
            $.ajax({
                type:'POST',
                url:'./leaderboard.py',
                success: function(data) {                                                     
                    console.log(data)
                };
            });
        }

        // Run the script when the page is fully loaded
        $(document).ready(function() {
            executePythonScript();
        });
```
