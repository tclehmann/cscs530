# Model Proposal for the Emergence and Evolution of Military Culture

Todd Lehmann

* Course ID: CMPLXSYS 530
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
Military culture is the set of norms that exist among military members about how to fight a war. The goal of this model is to explain why some military cultures lead to better organizational performance than others. Specifically, I intend to model the effects that different levels of trust stemming from recruitment methods (coercive vs. voluntary, class-based vs. non-class-based) and command structures (centralized vs. decentralized) have on the emergence of group-level beliefs about a state of nature, and explore how variations in trust can lead to either more or less accurate cultural norms.

&nbsp;  
### Justification
****

Complex systems are relevant for explaining military culture because cultural processes are inherently tied to interdependent social relationships, feedback loops, and adaptive processes. Therefore, agent-based models (ABMs) can be useful in specifying the micro-level interaction rules and structures that operate to develop an emergent organizational culture. In particular, militaries are large-scale, oftentimes distributed systems comprised of heterogeneous individuals that operate within a particular interaction structure, usually hierarchical. The interactions between individuals, and between individuals and their environment, can lead to macro-level emergent cultural properties that are not predicted by the individual-level interactions. By modeling the dynamics of military culture with an ABM, I therefore hope to evaluate the effects that different interaction structures, decision-rules, and distributions of agents have on the cultural consensus that emerges from the system of interactions.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

The main micro/macro processes I am interested in exploring are 1) how micro-level competition and coordination either encourage or discourage macro-level collaborative behavior, and 2) subsequently, how different levels of trust at the micro level lead to the emergence of a macro-level shared consensus that is either a better or worse representation of the true state of nature. 

To explore the micro-level processes, I will model individual agents that interact through a three-stage process consisting of 1) bargaining, 2) coordination, and 3) exchange of beliefs and updating based on trust levels. 

* Bargaining: Agents first face a bargaining problem in their interactions. If they are going to work together, they must first determine how they are going to allocate their resources and, by extension, how they will divide the gains that are captured following their efforts.

* Coordination: If agents can successfully agree on a bargaining solution, they then have to determine what strategy they are going to choose as a best response to all of their neighbors' strategies in a Stag Hunt game (alternatively, agents may choose to imitate the best strategy, rather than choose the best response strategically).

* Exchange of beliefs: Agents start out with an independent belief about the value for the true state of nature. If they can successfully bargain and coordinate their efforts with each other, they exchange beliefs with each other and learn new information about the state of nature. The new information is incorporated into an agent's beliefs based on the weight placed on its neighbor's beliefs, which represents the level of trust that one agent has in another agent.

The emergent macro-level dynamics of interest will consist of the extent to which information is both successfully exchanged throughout the organization, the extent to which the organization reaches full and correct consensus about the state of nature, and the speed at which consensus occurs.

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment

The static envirionment is fixed upon initialization, and is represented by 1) a payoff structure for agents playing a Stag Hunt game and 2) a truth value for the state of nature. If I were to model the environment dynamically, I could model it as changing payoffs and/or a changing state of nature, which would affect agents' best responses and updated beliefs, respectively. However, for the purposes of the present model, I am interested in simply 1) whether an organization can reach an accurate consensus about the state of nature and 2) the speed at which they reach this cultural consensus. Therefore, a static, exogenous environmental state suffices.

```python
payoff_map = {("S", "S"): (3.0,3.0), #Payoffs: Stag-Stag
             ("S", "H"): (0, 1.0),  #Payoffs: Stag-Hare
             ("H", "S"): (1.0, 0),  #Payoffs: Hare-Stag
             ("H", "H"): (1.0, 1.0)}  #Payoffs: Hare-Hare
    
m = 0.5  #Truth value for state of nature (mu) (in [0,1] for modeling convenience), about which agents receive a noisy signal initially
```

&nbsp; 

### 2) Agents
 
The agents in my model represent military members, or closely related communities of individuals that share the same behavior together and can be represented as a single agent, such as individual combat units.

Agent-owned variables include the following:
* Demand (a value that represents how much the agent demands in a divide-the-dollar bargaining game)
* State (an agent's strategy, i.e., whether an agent is playing 'Stag' or 'Hare' in the Stag Hunt coordination game)
* Previous payoffs (used to keep track of how well the agent has done in the past)
* Belief (the agent's belief about the value for the state of nature)

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

Agents interact as nodes in a fixed hierarchical network that is defined by the command structure that exists in military organizations. To represent a hierarchical network, I will construct the interaction topology as an ideal-type hierarchy, i.e., a balanced tree. Therefore, each node has a set number of subordinate nodes, and there are a set number of levels in the tree. For example, in a two-level balanced tree with six subordinates per node, the top-level leader (overall commander) supervises six nodes in level one (mid-level leaders), and each of these level-one nodes would have six of their own subordinates in level two (low-level soldiers).

Within this network, interactions operate over two neighborhoods: the interaction neighborhood (which extends to some specified path length in the network) and the imitation neighborhood (which extends only to the immediate neighborhood in the network). Agents are able to interact with any other agent within their interaction neighborhood, but they only imitate agents in their imitation neighborhood. 
 
**_Action Sequence_**

1. Step 1
2. Step 2
3. Etc...

&nbsp; 
### 4) Model Parameters and Initialization

_Describe and list any global parameters you will be applying in your model._

* Coercion level (if recruitment is coercive, 
* Class level (an agent's class identity, e.g., high-level officers come from upper class and low-level soldiers come from lower class)

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_
