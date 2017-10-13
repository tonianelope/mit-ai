from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.



def backchain_to_goal_tree(rules, hypothesis):
    #rules that result in hyp
    options = []
    op_i = 0

    #varibale stuff ?????

    for rule in rules:
        #print(rule)
        for con in rule.consequent():
            var = match(con, hypothesis)
            if(var or var == {}):
                options.append([])
                nomatch = False
                #print(rule.antecedent())

                ##if and/or loop else no loop!!!!!
                if(isinstance(rule.antecedent(), (list, tuple))):
                    for ant in rule.antecedent():
                        #get num of rules that make it up
                        res = (backchain_to_goal_tree(rules, populate(ant, var)))
                        #print(res, hypoth(?x) has rhythm and musicesis)
                        options[op_i].append(res)
                        #print(options)
                    if(isinstance(rule.antecedent(), AND)):
                        options[op_i] = (AND(options[op_i]))
                    else:
                        options[op_i] = (OR(options[op_i]))
                else:
                    res = (backchain_to_goal_tree(rules, populate(rule.antecedent(), var)))
                    #print(res, hypoth(?x) has rhythm and musicesis)
                    options[op_i] = (AND(res))
                op_i += 1

    options = OR([hypothesis]+[simplify(term) for term in options])

    #print(hypothesis)
    #print("G: ",simplify(options))
    return simplify(options)

# Here's an example of running the backward chainer - uncomment
# it to see it work:
#print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
