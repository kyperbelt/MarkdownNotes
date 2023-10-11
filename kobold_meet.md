---
title: Godot Sound Management System
---
# Godot Sound Management System

## Problem 
We don't have a simple way for the sound team to ealy integrate sounds into our games. Currently if a sound team member wants to include a sound effect or music, they must first add it to the scene graph through an AudioPlayer Node, and those get ingested by the `Bootleg AudioPlayer`. The audio player uses the name of the node to play the sound by name. Then the sound team member must manually adjust the volume and set the bus of each specific bus.

### Issues with current approach
- Rigid: Instrumenting change is tedious and requires manual work.
- Slow and Tedious: Implementing a single sound requires many steps. 
- Brittle: Changes to the name of audioplayers for example, can break calls where that sound was used. 
- Requires Sound team to have deep knowledge of how the engin works.


## Proposal

### Goals of this proposal
- Allow sound changes for sound to be done in a centralized place in the engine.
    - reduce the cognitive load required to integrate new sounds.
    - Integrate buses into this dashboard?
    - add effects to sounds
- Become resistant to changes. 
    - When a breaking change happens, we should be notified quickly and not only at the point of impact. 
        - **Example:** The sound no longer exists, we should not error out only when that sound is played, since this can be hard to find. 
- Easy to use.
- Allow bulk changes in grouped music and sounds.

### Requirements
| # | Story                                                                             | Priority |
| - | -                                                                                 | -        |
| 1 | As a sound team member I want an easy way to crossfade from one sound to another. | 0        |
| 2 | As a sound team member I want to be able create events that can be used by        | 0        |


### Design
#### Mockups
#### Architecture
