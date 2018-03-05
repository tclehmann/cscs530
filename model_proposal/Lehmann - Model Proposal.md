# Model Proposal for the Emergence and Evolution of Military Culture

Todd Lehmann

* Course ID: CMPLXSYS 530
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
Military culture is the set of shared norms among military members about how to fight a war. The goal of this model is to explain why some military cultures lead to better organizational performance than others. Specifically, I intend to model the effects that different recruitment methods (coercive vs. voluntary, class-based vs. non-class-based) and command structures (centralized vs. decentralized) have on the emergence of group-level beliefs about a state of nature, and show how variations in recruitment and command can lead to either more or less accurate group norms.

&nbsp;  
### Justification
****

Complex systems are relevant for explaining military culture because cultural processes are inherently tied to interdependent social relationships, feedback loops, and adaptive processes. Therefore, agent-based models (ABMs) can be useful in specifying the micro-level interaction rules and structures that operate to develop an emergent organizational culture. In particular, militaries are large-scale, oftentimes distributed systems comprised of heterogeneous individuals that operate within a particular interaction structure, usually hierarchical. The interactions between individuals, and between individuals and their environment, can lead to macro-level emergent cultural properties that are not predicted by the individual-level interactions. By modeling the dynamics of military culture with an ABM, I therefore hope to evaluate the effects that different interaction structures, decision-rules, and distributions of agents have on the cultural consensus that emerges from the system of interactions.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

The main micro/macro processes I am interested in exploring are 1) how micro-level competition and coordination either encourage or discourage macro-level collaborative behavior, and 2) subsequently, how different levels of trust at the micro level lead to the emergence of a macro-level shared consensus that is either a better or worse representation of the true state of nature. 

To explore the micro-level processes, I will model individual agents that interact through a three-stage processes consisting of 1) bargaining, 2) coordination, and 3) exchange of beliefs and updating based on trust levels. The emergent macro-level dynamics of interest will consist of the extent to which information is both successfully exchanged throughout the organization and the extent to which the organization reaches full and correct consensus about the state of nature.

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_Description of the environment in your model. Things to specify *if they apply*:_

* _Boundary conditions (e.g. wrapping, infinite, etc.)_
* _Dimensionality (e.g. 1D, 2D, etc.)_
* _List of environment-owned variables (e.g. resources, states, roughness)_
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your environment
# This may be a set of "patches-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any patch methods/procedures you have. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 2) Agents
 
 _Description of the "agents" in the system. Things to specify *if they apply*:_
 
* _List of agent-owned variables (e.g. age, heading, ID, etc.)_
* _List of agent-owned methods/procedures (e.g. move, consume, reproduce, die, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your agents
# This may be a set of "turtle-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any agent methods/procedures you have so far. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_Description of the topology of who interacts with whom in the system. Perfectly mixed? Spatial proximity? Along a network? CA neighborhood?_
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. Step 1
2. Step 2
3. Etc...

&nbsp; 
### 4) Model Parameters and Initialization

_Describe and list any global parameters you will be applying in your model._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_
