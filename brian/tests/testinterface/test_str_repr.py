from brian import *

def test_str_repr():
    ''' 
    Tests that the __str__ and __repr__ methods work for the most important
    Brian classes. This only tests whether they return any string at all.
    (For units this is tested in test_units.py)
    '''
    
    def assert_str_repr(obj):
        assert(len(str(obj)))
        assert(len(repr(obj)))               
    
    # Clocks
    clock = Clock(dt=0.2*ms)
    assert_str_repr(clock)
    assert_str_repr(defaultclock)    
    
    # Equations and NeuronGroups    
    eqs = Equations('dv/dt=-v/(5 * ms) : volt')
    group = NeuronGroup(100, model=eqs, reset=0*mV, threshold=10*mV)
    assert_str_repr(eqs)
    assert_str_repr(group)
    
    subg = group.subgroup(50)
    assert_str_repr(subg)
    
    pgroup = PoissonGroup(1, rates=100*Hz)
    assert_str_repr(pgroup)
    
    sgroup = SpikeGeneratorGroup(1, [])
    assert_str_repr(sgroup)
    
    # Thresholds and Resets
    thresholds = [Threshold(1), StringThreshold('v > 1'),
                  VariableThreshold('v', 'w')]
    for threshold in thresholds:
        assert_str_repr(threshold)

    resets = [Reset(0), StringReset('v = 0')]
    for reset in resets:
        assert_str_repr(reset)

    # Connections
    con = Connection(group, group, 'v')
    con.connect_full(group, group, 1*mvolt)
    assert_str_repr(con)
    
    con_delay = Connection(group, group, 'v', delay=True)
    con_delay.connect_full(group, group, weight=1*mvolt, delay=5*ms)
    assert_str_repr(con_delay)
        
    # Monitors and counters
    monitors = [SpikeMonitor(group), StateMonitor(group, 'v'),
                SpikeCounter(group), StateSpikeMonitor(group, 'v'),
                RecentStateMonitor(group, 'v'), MultiStateMonitor(group),
                PopulationRateMonitor(group), PopulationSpikeCounter(group),
                CoincidenceCounter(group, [1*ms, 2*ms]), VanRossumMetric(group)]
    for monitor in monitors:
        assert_str_repr(monitor)

    # Networks
    net = MagicNetwork()
    assert_str_repr(net)
    
    net = Network(group, con)
    assert_str_repr(net)

if __name__ == '__main__':
    test_str_repr()