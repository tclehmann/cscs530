# Model Proposal for the Emergence and Evolution of Military Culture

Todd Lehmann

* Course ID: CMPLXSYS 530
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018

&nbsp; 

__*LS COMMENTS:*__
*I really like your conceptual approach in general here, especially vis-a-vis honing in on how coordination in action often acts as precursor for belief sharing and cultural consensus/social cohesion and the potential role of hierarchical structure in that process. Currently though, I think you might be trying to do too many things all at once with this model. Having 3 layers of interaction going on (Bargaining, Stag Hunt, Belief updating) in addition with 2 potential pathways for choosing strategies (imitate and best response), two types of neighborhoods to consider (imitation and game play) and additional variables which will also be affecting interaction (coercion and class) as well as choices about hierarchical structure are all baking in a bunch of assumptions that will make it hard to disentangle what is going on in the model (let along set you up for a huge amount of coding, a really complicated debugging process, massive amounts of analysis, etc.)*

*My suggestions in this regard might be to try to find a way to start way simpler, maybe with just updating a stag-hunt game on a network with memory where individuals just use their neighbors' prior decisions as the basis for their best guess of what to choose next turn. From there, you can then add another layer of belief updating wherein successful coordination between individuals leads to either less noisy or more strongly weighted communications on updating belief. That is just one possible route to go - there are others as well. Definitely though I would suggest slimming this model down a good bit and getting something simple running really well first and then building out from there. It will not only make your job easier in the immediacy, it will greatly strengthen any conclusions you end up drawing and make verification worlds easier.*


&nbsp; 

### Goal 
*****
 
Military culture is the set of norms that exist among military members about how to fight a war. The goal of this model is to explain why some military cultures lead to better organizational performance than others. Specifically, I intend to model the effects that different levels of trust between agents stemming from recruitment methods (coercive vs. voluntary, class-based vs. non-class-based) have on the emergence of group-level beliefs (representing cultural norms) about a state of nature, and explore how variations in trust can lead to either more or less accurate cultural norms.

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

The static envirionment is fixed at initialization, and is represented by 1) a payoff structure for agents playing a Stag Hunt game and 2) a truth value for the state of nature. If I were to model the environment dynamically, I could incorporate changing payoffs and/or a changing state of nature, which would affect agents' best responses and beliefs, respectively. However, for the purposes of the present model, I am interested in simply 1) whether an organization can reach an accurate consensus about the state of nature and 2) the speed at which they reach this cultural consensus. Therefore, a static, exogenous environmental state suffices.

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
* Belief (the agent's belief about the true value for the state of nature)

Additionally, agents have fixed attributes that are used to update their beliefs when interacting with other agents:
* Coercion level (if recruitment is coercive or voluntary)
* Hierarchy level (an agent's position in the hierarchy based on its level)
* Class level (an agent's class identity, e.g., high-level officers come from upper class and low-level soldiers come from lower class)

&nbsp;



```python
import numpy.random as RD
import networkx as NX
from scipy.stats import norm

#Assign initial attributes for each agent
    for n in network.nodes_iter():
        network.node[n]['state'] = 0
        network.node[n]['previous_payoffs'] = []
        network.node[n]['demand'] = RD.random()
        network.node[n]['belief'] = norm.ppf(RD.uniform(low=norm.cdf(0, m, s), high=norm.cdf(1, m, s), size=1), m, s)
        #The above truncates the normal distribution between 0 and 1 to make distribution of beliefs easier to interpret
        
    #PSEUDOCODE:
      for each node at each level, assign coercion, hierarchy, and class attributes
```

Agent-owned procedures exist for the Stag Hunt coordiation game. Agents either choose a best response to their neighbors' expected strategies (based on bargaining outcome), or they choose to imitate the most successful neighbor's strategy.

&nbsp;

__*LS COMMENTS:*__
*I was not sure from the the below if "neighbors" here meant only one's immediate neighbors or all other nodes who are reachable in a certain number of steps? single_source_shortest_path_length() will give the shortest distance to all other nodes in the connected component of a network (though there is an optional argument "cutoff" which will return only nodes that are <= that number of steps away). If you only want immediate neighbors, you can also just use the "neighbors(nodeID)" function.*

```python
def best_response(n):  ##BEST RESPONSE PROCEDURE
    #Determine interaction structure based on shortest path length
    br_path=NX.single_source_shortest_path_length(network,n)
    br_path_list = dict((k, v) for k, v in br_path.items() if v <= br_path_length)

    #Count the number of neighbors potentially playing Stag following bargaining game
    total = 0
    nbs = list(br_path_list.keys())
    for nb in nbs:
        if network.node[n]['demand'] + network.node[nb]['demand'] <= 1:
            total += network.node[nb]['state']

    ### LS COMMENTS ###
    # Wasn't entirely clear here on how the bargaining game interacts with the Stag-hunt one. May just need some more explanation of 
    # what some of these variables are doing and/or how they are being updated.
    
    #Calculate expected payoff for playing Stag against each strategy
    stag_exp_payoff = total * SS_selfpayoff * network.node[n]['demand'] + (len(nbs) - total) * SH_selfpayoff

    #Calculate expected payoff for playing Hare
    hare_exp_payoff = total * HS_selfpayoff + (len(nbs) - total) * HH_selfpayoff

    #Choose best response strategy based on expected payoff
    if hare_exp_payoff < stag_exp_payoff:
        nextNetwork.node[n]['state'] = 1
        network.node[n]['previous_payoffs'].append(stag_exp_payoff)
        nextNetwork.node[n]['demand'] = network.node[n]['demand']
    elif hare_exp_payoff > stag_exp_payoff:
        nextNetwork.node[n]['state'] = 0
        network.node[n]['previous_payoffs'].append(hare_exp_payoff)
        nextNetwork.node[n]['demand'] = RD.random()
    elif hare_exp_payoff == stag_exp_payoff:
        nextNetwork.node[n]['state'] = RD.choice([0, 1])
        network.node[n]['previous_payoffs'].append(stag_exp_payoff)
        nextNetwork.node[n]['demand'] = network.node[n]['demand']

def imitate_best(n):  ##IMITATE THE BEST PROCEDURE
    #Determine imitation structure based on shortest path length
    imitate_path=NX.single_source_shortest_path_length(network,n)
    imitate_path_list = dict((k, v) for k, v in imitate_path.items() if v <= imitate_path_length)

    #Start with own total payoff, strategy, and demand
    highest_payoff = sum(network.node[n]['previous_payoffs'])
    current_strategy = nextNetwork.node[n]['state']
    current_demand = nextNetwork.node[n]['demand']

    #Compare to each neighbor's payoff. If one is higher, switch to that neighbor's strategy.
    #During this, also count the number of neighbors playing Stag.
    total = 0
    nbs = list(imitate_path_list.keys())
    for nb in nbs:
        total += network.node[nb]['state']
        if highest_payoff < sum(network.node[nb]['previous_payoffs']):
            highest_payoff = sum(network.node[nb]['previous_payoffs'])
            nextNetwork.node[n]['state'] = network.node[nb]['state']
            current_strategy = nextNetwork.node[n]['state']
            nextNetwork.node[n]['demand'] = network.node[nb]['demand']
            current_demand = nextNetwork.node[n]['demand']
            
    #Update payoff history
    if current_strategy == 1:
        #Calculate expected payoff for playing Stag
        stag_exp_payoff = total * SS_selfpayoff * current_demand + (len(nbs) - total) * SH_selfpayoff
        network.node[n]['previous_payoffs'].append(stag_exp_payoff)
        nextNetwork.node[n]['demand'] = current_demand
    elif current_strategy == 0:
        #Calculate expected payoff for playing Hare
        hare_exp_payoff = total * HS_selfpayoff + (len(nbs) - total) * HH_selfpayoff
        network.node[n]['previous_payoffs'].append(hare_exp_payoff)
        nextNetwork.node[n]['demand'] = current_demand

def update_belief(n):
    #For each neighbor with which an agent plays "Stag," exchange beliefs and update own belief based on level of trust in each neighbor
    
    ## LS COMMENTS###
    # Is this true even if the individual played Hare? May need to discuss the motivation for this decision a bit more.
    
    
    #Determine interaction structure based on shortest path length
    br_path=NX.single_source_shortest_path_length(network,n)
    br_path_list = dict((k, v) for k, v in br_path.items() if v <= br_path_length)

    #Get the set of neighbors that played Stag this round
    nbs = list(br_path_list.keys())
    
    stag_neighbors_list = []
        
    for nb in nbs:
        if network.node[nb]['state'] == 1:
            stag_neighbors_list.append(nb)
    
    #PSEUDOCODE:
    #Compute weighted belief updated based upon trust in own belief and trust in other neighbors' beliefs, which
    #are determined by recruitment methods
    for each Stag-playing neighbor, determine its class/coercion value, and apply assigned weighting to its belief value
    update own belief based on weighted sum of own and neighbors' beliefs
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

Agents interact as nodes in a fixed hierarchical network that is defined by the command structure that exists in military organizations. To represent a hierarchical network, I will construct the interaction topology as an ideal-type hierarchy, i.e., a balanced tree. Therefore, each node has a set number of subordinate nodes, and there are a set number of levels in the tree. For example, in a two-level balanced tree with six subordinates per node, the top-level leader (overall commander) supervises six nodes in level one (mid-level leaders), and each of these level-one nodes would have six of their own subordinates in level two (low-level soldiers).

```python
import networkx as NX

# Create a balanced tree graph (hierarchical structure)
sup = supervised
lev = levels
network = NX.balanced_tree(sup,lev)
```

Within this network, interactions operate over two neighborhoods: the interaction neighborhood (which extends to some specified path length in the network) and the imitation neighborhood (which may extend to a different specified path length in the network, e.g., only to the immediate neighborhood in the network). Agents are able to interact with any other agent within their interaction neighborhood, but they only imitate agents in their imitation neighborhood. 
 
**_Action Sequence_**
nbsp;

__*LS COMMENTS:*__
*See previous comments regarding modeling simplification*


1. An agent probabilistically chooses either the "best response" procedure or the "imitate the best" procedure. The probability of each procedure is set at the beginning of the simulation.
2. For the "best response" procedure, each agent determines the expected payoffs for playing "Stag" or "Hare" this round based on the outcome of the divide-the-dollar bargaining game. (NOTE: This bargaining problem can be elevated to a higher level in the hierarchy if command is more centralized, thereby removing the bargaining problem at lower levels). If bargaining is successful, an agent expects its neighbor to play Stag, otherwise the agent expects its neighbor to play Hare. The agent then chooses the strategy that provides the highest expected payoff when played against all its neighbors' expected strategies. 
3. For the "imitate the best" procedure, each agent considers the total payoffs that its neighbors currently hold, and chooses the strategy and bargaining demand yielding the highest total payoff.
4. All agents update their strategies, payoffs received, and bargaining demands sychronously.
5. For all neighbors with which an agent plays "Stag-Stag" in this round, the agent observes its neighbors' beliefs and updates its own belief based on its level of trust for each neighbor. This procedure is also updated synchronously. 

```python
def step():
    global time, network, nextNetwork

    time += 1
            
    dynamics_draw = RD.random()
    
    if dynamics_draw > prob_imitate:     ###BEST RESPONSE DYNAMICS###
    
    #For each agent, determine payoffs of playing each strategy this round based on neighbors' previous strategies,
    #then choose best response
    
        for n in network.nodes_iter():
            
            network.node[n]['previous_payoffs'] = network.node[n]['previous_payoffs'][:memory]
            
            best_response(n)

    else:  ###IMITATE THE BEST DYNAMICS###

        #For each agent, compare own total payoff to each neighbor's total payoff. Choose the strategy
        #that matches the highest total payoff.
        
        for n in network.nodes_iter():
            
            network.node[n]['previous_payoffs'] = network.node[n]['previous_payoffs'][:memory]
            
            imitate_best(n)
                    
    network, nextNetwork = nextNetwork, network
    
    #PSEUDOCODE:
    #For each agent, update beliefs
    
    #for n in network.nodes_iter():
        #update_beliefs(n)
```

&nbsp; 
### 4) Model Parameters and Initialization

Global parameters include time, network (which includes nodes, edges, and node attributes), and next network (which serves as a placeholder for current iteration updates).

Before initializing, the user specifies Stag Hunt payoff values, state of nature truth value, noise term (standard deviation of a Normal distribution with mean zero), probability of "imitate the best" procedure (where the probability of "best response" is 1 minus this value), agents' memory (number of rounds each agent keeps track of payoffs), the structure of the balanced tree, the interaction and imitation structures (specified as the path length from each agent that an interaction can occur), and if desired, an initial number of Stag players (otherwise, randomly assigned).

Upon initialization, the network is constructed as a balanced tree as specified by the user, and each agent is assigned a level of bargaining demand, strategy, and belief about the state of nature (which is based on a noisy signal of the true value). 

During each iteration, the action sequence described above is executed for each agent. All agents update their bargaining demands, strategies, payoffs received, and beliefs synchronously.

```python
import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
#import random as RD
import numpy.random as RD
import matplotlib.pyplot as plt
from scipy.stats import norm

#VARIABLES:
payoff_map = {("S", "S"): (3.0,3.0), #Payoffs: Stag-Stag
             ("S", "H"): (0, 1.0),  #Payoffs: Stag-Hare
             ("H", "S"): (1.0, 0),  #Payoffs: Hare-Stag
             ("H", "H"): (1.0, 1.0)}  #Payoffs: Hare-Hare
    
m = 0.5  #Truth value for state of nature (mu), about which agents receive a noisy signal initially (in [0,1])
s = 0.2  #Noise term (e_i) for agent's state of nature signal (normally distributed with expectation zero)

prob_imitate = 0.10 #Probability that imitate-the-best dynamics are selected at each iteration
memory = 3  #Number of rounds each agent keeps track of payoffs
    
supervised = 6 #Number of agents supervised at each level
levels = 2 #Number of levels (excluding top overall leader)

#For the following path length variables, min = 1, max = 2*levels
br_path_length = 2 #Number of paths a best-response interaction can span in the network for a given agent
imitate_path_length = 2 #Number of paths an imitate-the-best interaction can span in the network for a given agent

init_stag = 1  #Initial number of Stag players (Min = 1, max = total agents - 1)

SS_selfpayoff, SS_otherpayoff = payoff_map[("S", "S")]
SH_selfpayoff, SH_otherpayoff = payoff_map[("S", "H")]
HS_selfpayoff, HS_otherpayoff = payoff_map[("H", "S")]
HH_selfpayoff, HH_otherpayoff = payoff_map[("H", "H")]

demand_lower = HH_selfpayoff/(SS_selfpayoff + SS_otherpayoff)

RD.seed()

col = {0:'r', 1:'k'} #Hare strategies are red, Stag strategies are black

def init():
    global time, network, nextNetwork, positions

    time = 0
    
    # Create a balanced tree graph (hierarchical structure)
    sup = supervised
    lev = levels
    network = NX.balanced_tree(sup,lev)
    
    #Assign initial attributes for each agent
    for n in network.nodes_iter():
        network.node[n]['state'] = 0
        network.node[n]['previous_payoffs'] = []
        #network.node[n]['demand'] = RD.uniform(demand_lower,1-demand_lower)
        network.node[n]['demand'] = RD.random()
        network.node[n]['belief'] = norm.ppf(RD.uniform(low=norm.cdf(0, m, s), high=norm.cdf(1, m, s), size=1), m, s)
        #The above truncates the normal distribution between 0 and 1 to make distribution of beliefs easier to interpret
        
    #Assign initial number of Stag players
    stags = RD.sample(network.nodes(),init_stag)
    for stag in stags:
        network.node[stag]['state'] = 1

    nextNetwork = network.copy()

    positions = NX.spring_layout(network)
```

&nbsp; 

### 5) Assessment and Outcome Measures

To assess my model outcomes, I will focus on the time it takes for agents to come to a consensus about their beliefs, and the difference between the value of their beliefs and the value of the truth. I will also build in a limit to the number of iterations the simulation runs, should agents never reach a consensus.

Additionally, I will assess the outcomes described above for different levels of bargaining centralization. Instead of having each agent bargain in a decentralized manner, I will model a more centralized process that removes bargaining at lower levels, in order to reduce bargaining conflict and encourage cooperation and coordination. In doing so, I will also incorporate more weight on the centralized figures' own beliefs to further account for these centralization pressures, and measure the effect that such centralization has on the organization's cultural consensus that emerges.

&nbsp; 

### 6) Parameter Sweep

I am most interested in sweeping the following parameters:

* Truth value in [0,1]
* Noise term (standard deviation for the truth value, normally distributed with mean zero) in (0,1]
* Probability of imitation versus best response in (0, 1)
* Number supervised (2 to 10) and number of levels (1 to 3) for the balanced tree
* Best response path length (value from 1 to 2 times the number of levels in the tree)
* Imitation path length (value from 1 to 2 times the number of levels in the tree)
* Initial number of Stag players (from zero to all agents in a given tree)
