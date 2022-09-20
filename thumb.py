import getpass 
import argparse
import pylab 
from numpy import linspace, pi 

parser = argparse.ArgumentParser(description = "Add name")
parser.add_argument("--name", default="name", type=str)
args = parser.parse_args()

lusr = getpass.getuser()
file_name = args.name 

record = dict()
record["DIR"] = "/home/" +  lusr + "/solidphase/inputs/pack/" + file_name

circ = linspace(0,2*pi)
fig = pylab.figure()
ax=fig.add_subplot()
ax.set_aspect(1)
vol_sph = 0.0
for x0 in result:
    x = x0[0]
    y = x0[1]
    z = x0[2]
    f3d.write("{} {} {} {}\n".format(x,y,z,radius));

    if abs(z) > radius: continue
    
    reff = sqrt(abs(radius**2 - z**2))

    vol_sph = vol_sph + pi*reff**2
    
    f2d.write("{} {} {} {}\n".format(x,y,z,reff))

    ax.plot(x+reff*cos(circ),y+reff*sin(circ))

fig.savefig(record['DIR']+"/thumbnail.png")

