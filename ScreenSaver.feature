Feature: screensaver on the touchscreens

    Scenario Outline: User changes the sleep time
        Given sysman client
        When user changes sleep time to <time>
        Then Android screensaver settings should be set to <time> <result>

    Examples: Times
        | time | result |
        | 0    | fail   |
        | 30   | pass   |
        | 60   | pass   |
