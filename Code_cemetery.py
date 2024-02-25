'''
When code doesn't work out, but I put enough effort into it to be sad to delete it, it goes here.
I swear I'm not a hoarder.
'''

'''
These are position functions for an electron in hhg which didn't quite work, either because I got the wrong constants or 
I just made an error somewhere (needs you to define quite a few constants)
'''
sin_term = (charge*energy_i/(mass*angular_v))*(time-time_i)*sin(angular_v*time + phase)
position =  (-charge/(mass*angular_v**2))*(energy*cos(angular_v*time + phase) - energy_i*cos(angular_v*time_i + phase)) - sin_term
position = ((-charge*E_0)/(mass*angular_v**2))*cos(angular_v*time + phase) + (-(charge*E_0)/(mass*angular_v**2))

