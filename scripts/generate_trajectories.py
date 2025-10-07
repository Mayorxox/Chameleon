#!/usr/bin/env python3
"""Generate example proxemic trajectories (JSON)"""
import json, os, numpy as np

OUT = 'data/trajectories'
os.makedirs(OUT, exist_ok=True)

def generate(zone='social', duration=10, fps=15):
    t = np.linspace(0, duration, int(duration*fps))
    if zone == 'personal':
        d = 0.45 + 0.5*np.sin(2*np.pi*t/duration)
    elif zone == 'social':
        d = 1.2 + 0.6*np.sin(2*np.pi*t/duration)
    else:
        d = 3.5 + 0.2*np.sin(2*np.pi*t/duration)
    v = np.gradient(d, t)
    angle = np.deg2rad(np.random.uniform(-10,10,len(t)))
    traj = [{'t': float(tt), 'd': float(dd), 'v': float(vv), 'theta': float(a)} for tt,dd,vv,a in zip(t,d,v,angle)]
    return traj

if __name__ == '__main__':
    for z in ['personal','social','public']:
        traj = generate(zone=z, duration=8, fps=15)
        fname = os.path.join(OUT, f'trajectory_{z}.json')
        with open(fname,'w') as f:
            json.dump(traj, f, indent=2)
        print('Wrote', fname)
