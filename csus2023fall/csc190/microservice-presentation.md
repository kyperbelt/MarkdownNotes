---
title: CSC190 Mircoservice Architecture | Benefits of Ownership
author: Jonathan Camarena Camacho
---

# CSC190 Mircoservice Architecture | Benefits of Ownership

## Breath of Knowldege
A lot of you expressed interest in learning and gaining experience with more than one of these technologies. By breaking down the project strcutre into a set of separate services we are able to give each  
* Architecture and Design
* Presentation Skills
* Containarization
* Database
* API

@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml

## Other Benefits

* **Domain Expertise**
    By giving focusing a person(s) on solving a single problem, they are better able to develop domain expertise. You will better know your problem space and act instead of react.

* **Problem Encapsulation**
When these services are decoupled, we can better debug issues. For example, say we have a problem with loging in, we can quickly pinpoint the issue in the login&authorization service(s).

* **Freedom to Design**
Last but no least, Having smaller teams allows those teams to take ownership and choose how they design a solution to attack the problem. As long as contracts(API) are maintained then other services do not really care how the underlying service is implemented. 

## Posible team Layouts 1
Each member of the team owns their own service and is in charge of maintaing API contracts. 

* **Constraint**: 
    - Must use same language for ease of code review by other members of the team.
    - Communication with other members of the team is crucial.

* **Pros**:
    - Wider breadth of expertise from setting up a backend service.
    - More freedom to design.

* **Cons**: 
    - Duplication 
        > :warning: We can fight this by sharing knowledge across services
        - Responsibility
        - Code 
        - Technologies

## Posible team Layouts 1
We consolidate the microservices down to 2-3 and have teams of 2-3 tackle each one. 

* **Constraint**: 
    - Same langauge is not required because you will have members in your subteam who will be able to code review you.
    - 

* **Pros**:
    - More people to bounce off of.
    - Less Duplication

* **Cons**: 
    - C
