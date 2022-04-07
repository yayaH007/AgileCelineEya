Feature: buy a cookie

  Scenario Outline: buy something
    Given I buy a <taste> cookie
    When I check for pepites
    Then the pepites number is   <nb_pepite>


    Examples:
     | taste      |nb_pepite   |
     | choco      |100         |
     | sans choco |0           |
