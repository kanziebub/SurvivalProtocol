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

<script>
  // Define a function to execute the script
  function executePythonScript() {
    $.post('/run_script', function(data) {
      console.log(data); // Display the response from the server
    });
  }

  // Run the script when the page is fully loaded
  $(document).ready(function() {
    executePythonScript();
  });
</script>
