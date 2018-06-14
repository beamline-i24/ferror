import epics
import subprocess

motor_dict = {
 1 : ['BL24I-OP-DCM-01:BRAGG'      ],\
 2 : ['BL24I-OP-DCM-01:T2'         ],\
 3 : ['BL24I-OP-DCM-01:ROLL'       ],\
 4 : ['BL24I-OP-DCM-01:PITCH'      ],\
 5 : ['BL24I-AL-SLITS-01:X:GAP'    ],\
 6 : ['BL24I-AL-SLITS-01:X:INBOARD'],\
 7 : ['BL24I-AL-SLITS-01:Y:GAP'    ],\
 8 : ['BL24I-AL-SLITS-01:Y:BOTTOM' ],\
 9 : ['BL24I-AL-SLITS-02:X:PLUS'   ],\
10 : ['BL24I-AL-SLITS-02:X:MINUS'  ],\
11 : ['BL24I-AL-SLITS-02:Y:PLUS'   ],\
12 : ['BL24I-AL-SLITS-02:Y:MINUS'  ],\
13 : ['BL24I-DI-QBPM-01:FOIL'      ],\
14 : ['BL24I-OP-HPFM-01:Y1'        ],\
15 : ['BL24I-OP-HPFM-01:Y2'        ],\
16 : ['BL24I-OP-HPFM-01:Y3'        ],\
17 : ['BL24I-OP-HPFM-01:X1'        ],\
18 : ['BL24I-OP-HPFM-01:X2'        ],\
19 : ['BL24I-DI-PHDGN-01:Y'        ],\
20 : ['BL24I-OP-VPFM-01:Y1'        ],\
21 : ['BL24I-OP-VPFM-01:Y2'        ],\
22 : ['BL24I-OP-VPFM-01:Y3'        ],\
23 : ['BL24I-OP-VPFM-01:X1'        ],\
24 : ['BL24I-OP-VPFM-01:X2'        ],\
25 : ['BL24I-DI-QBPM-02:FOIL'      ],\
26 : ['BL24I-DI-QBPM-03:FOIL'      ],\
27 : ['BL24I-AL-SLITS-03:X:GAP'    ],\
28 : ['BL24I-AL-SLITS-03:X:INBOARD'],\
29 : ['BL24I-AL-SLITS-03:Y:GAP'    ],\
30 : ['BL24I-AL-SLITS-03:Y:BOTTOM' ],\
31 : ['BL24I-AL-SLITS-04:X:GAP'    ],\
32 : ['BL24I-AL-SLITS-04:X:INBOARD'],\
33 : ['BL24I-AL-SLITS-04:Y:GAP'    ],\
34 : ['BL24I-AL-SLITS-04:Y:BOTTOM' ],\
35 : ['BL24I-OP-VMFM-01:PITCH'     ],\
36 : ['BL24I-OP-VMFM-01:Y'         ],\
37 : ['BL24I-OP-HMFM-01:PITCH'     ],\
38 : ['BL24I-OP-HMFM-01:Y'         ],\
39 : ['BL24I-EA-DET-01:Z'          ],\
40 : ['BL24I-EA-DET-01:Y'          ],\
41 : ['BL24I-MO-TRAY-01:Y'         ],\
42 : ['BL24I-MO-TRAY-01:Z'         ],\
43 : ['BL24I-MO-GONIO-01:TTABY'    ],\
44 : ['BL24I-MO-TABLE-01:X1'       ],\
45 : ['BL24I-MO-TABLE-01:X2'       ],\
46 : ['BL24I-MO-LIGHT-01:Y'        ],\
47 : ['BL24I-MO-GONIO-01:OMEGA'    ],\
48 : ['BL24I-MO-GONIO-01:TTABX'    ],\
49 : ['BL24I-MO-GONIO-01:TTABZ'    ],\
50 : ['BL24I-OP-ATTN-01:DISC1'     ],\
51 : ['BL24I-OP-ATTN-01:DISC2'     ],\
52 : ['BL24I-DI-QBPM-04:DISC'      ],\
53 : ['BL24I-OP-VMFM-01:X'         ],\
54 : ['BL24I-OP-HMFM-01:X'         ],\
55 : ['BL24I-OP-MTAB-01:Z'         ],\
56 : ['BL24I-CG-JET-01:TRANS'      ],\
57 : ['BL24I-MO-GONIO-02:PINZS'    ],\
58 : ['BL24I-MO-GONIO-02:OMEGA'    ],\
59 : ['BL24I-MO-GONIO-02:PINXS'    ],\
60 : ['BL24I-MO-GONIO-02:KAPPA'    ],\
60 : ['BL24I-MO-GONIO-02:PHI'      ],\
61 : ['BL24I-MO-VPIN-01:X'         ],\
62 : ['BL24I-MO-VPIN-01:Z'         ],\
63 : ['BL24I-MO-GONIO-02:PINY'     ],\
64 : ['BL24I-MO-VPIN-01:Y'         ],\
65 : ['BL24I-AL-SLITS-05:X:PLUS'   ],\
66 : ['BL24I-AL-SLITS-05:X:MINUS'  ],\
67 : ['BL24I-AL-SLITS-05:Y:PLUS'   ],\
68 : ['BL24I-AL-SLITS-05:Y:MINUS'  ],\
69 : ['BL24I-AL-GUARD-01:X'        ],\
70 : ['BL24I-AL-GUARD-01:Y'        ],\
71 : ['BL24I-AL-APTR-01:X'         ],\
72 : ['BL24I-AL-APTR-01:Y'         ],\
73 : ['BL24I-RS-ABSB-02:X'         ],\
74 : ['BL24I-RS-ABSB-02:Y'         ],\
75 : ['BL24I-RS-ABSB-02:Z'         ],\
76 : ['BL24I-RS-ABSB-02:ROTY'      ],\
77 : ['BL24I-MO-GONIO-02:PINYH'    ]} 

for k, v in motor_dict.items():
    print k, v

motor_choice = raw_input('Choose a motor or motors separated by a space: ').rstrip(' ')
motor_pv_list = [motor_dict[int(x)][0] for x in motor_choice.split(' ')] 
print motor_pv_list
motor_pv = motor_pv_list[0]

mtr = epics.PV(motor_pv)
print mtr.info

g = open('tmp.stp', 'w')
g.write('StripConfig                   1.2   \n')
g.write('Strip.Time.Timespan           30    \n')
g.write('Strip.Time.NumSamples         7200  \n')
g.write('Strip.Time.SampleInterval     0.1   \n')
g.write('Strip.Time.RefreshInterval    0.1   \n')

g.write('Strip.Curve.0.Name            %s.RBV    \n' %motor_pv)
g.write('Strip.Curve.0.Units           %s        \n' %mtr.units)
g.write('Strip.Curve.0.Precision       %s        \n' %mtr.precision)

g.write('Strip.Curve.1.Name            %s:FERROR    \n' %motor_pv)
g.write('Strip.Curve.1.Units           %s           \n' %mtr.units)
g.write('Strip.Curve.1.Precision       %s           \n' %mtr.precision)
g.write('Strip.Curve.1.Min             0.0          \n')
g.write('Strip.Curve.1.Max             0.1          \n')

g.write('Strip.Curve.2.Name            %s.VAL    \n' %motor_pv)
g.write('Strip.Curve.2.Units           %s        \n' %mtr.units)
g.write('Strip.Curve.2.Precision       %s        \n' %mtr.precision)

g.close()

subprocess.call(['StripTool','tmp.stp'])

print 'EOP'
