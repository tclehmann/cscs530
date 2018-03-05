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

To explore the micro-level processes, I will model individual agents that interact through a three-stage process consisting of 1) bargaining, 2) coordination, and 3) exchange of beliefs and updating based on trust levels. The emergent macro-level dynamics of interest will consist of the extent to which information is both successfully exchanged throughout the organization and the extent to which the organization reaches full and correct consensus about the state of nature.

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment

The static envirionment is fixed upon initialization, and is represented by 1) a payoff structure for agents playing a Stag Hunt game and 2) a truth value for the state of nature. I am interested in both 1) whether an organization can reach an accurate consensus about the state of nature and 2) the speed at which they reach this cultural consensus. Therefore, if I were to model the environment dynamically, I could model it as changing payoffs and/or a changing state of nature that changes more or less frequently, which would affect agents' best responses and updated beliefs, respectively, after a certain period of time. However, for the purposes of the present model, a static, exogenous environmental state suffices.

```python
payoff_map = {("S", "S"): (3.0,3.0), #Payoffs: Stag-Stag
             ("S", "H"): (0, 1.0),  #Payoffs: Stag-Hare
             ("H", "S"): (1.0, 0),  #Payoffs: Hare-Stag
             ("H", "H"): (1.0, 1.0)}  #Payoffs: Hare-Hare
    
m = 0.5  #Truth value for state of nature (mu) (in [0,1] for modeling convenience), about which agents receive a noisy signal initially
```

&nbsp; 

### 2) Agents
 
Agents are nodes in a hierarchical network that represent either individuals or sub-units of the organization. 

Agent-owned variables include the following:
* _State (whether an agent is currently playing either Stag or Hare in the Stag Hunt coordination game)
*_Previous payoffs (used to keep track of how well the agent has done in the past)
*_Demand (a value between 0 and 1 that represents how much the agent demands in the divide-the-dollar bargaining game)
*_Belief (the agent's belief about the value for the state of nature)

There are no agent-owned procedures. All updating occurs via agent interactions.

```python
#Assign initial attributes for each agent
    for n in network.nodes_iter():
        network.node[n]['state'] = 0
        network.node[n]['previous_payoffs'] = []
        network.node[n]['demand'] = RD.random()
        network.node[n]['belief'] = norm.ppf(RD.uniform(low=norm.cdf(0, m, s), high=norm.cdf(1, m, s), size=1), m, s)
        #The above truncates the normal distribution between 0 and 1 to make distribution of beliefs easier to interpret
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
