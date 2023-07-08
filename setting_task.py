# Parameter Setting on tasks, from task 1 to task 4
# the area is 1000 * 1000, each subarea is 100 * 100, totally 100 subareas

# diffusion weight of differet tasks
taskWeights = {1: 0.3, 2: 0.5, 3: 0.4, 4: 0.4}

qualityOfSubarea = {1: {1: 0.14337620735375034, 2: 0.21082057287593092, 3: 0.956523852428056, 4: 0.1278683729700073, 5: 0.04355537673771359, 6: 0.28015393503211095, 7: 0.39646382189091434, 8: 0.008452979479723677, 9: 0.3970979949725515, 10: 0.47628813873566145, 11: 0.6648815144319103, 12: 0.43028215481561327, 13: 0.9562080567091992, 14: 0.9217624715429521, 15: 0.4772842693441576, 16: 0.40675829860863333, 17: 0.991640814977722, 18: 0.023993976105067816, 19: 0.5575492938240441, 20: 0.31363263620413195, 21: 0.821978951919411, 22: 0.8564861932164695, 23: 0.3588856190779276, 24: 0.7254850297408828, 25: 0.4083793259125006, 26: 0.8664463237387109, 27: 0.9012236831380936, 28: 0.29199230860864267, 29: 0.28044370157857723, 30: 0.7494845002665877, 31: 0.1604018032431329, 32: 0.44346254226078674, 33: 0.8708611541929402, 34: 0.020980398778602916, 35: 0.44410609618219454, 36: 0.2462609437649137, 37: 0.11462689489299449, 38: 0.8847151684478675, 39: 0.13935081418858264, 40: 0.5515756268374434, 41: 0.5502110912203149, 42: 0.8401315476475474, 43: 0.2205667945023202, 44: 0.0239632630585056, 45: 0.95731610874541, 46: 0.19446150972333787, 47: 0.5971940157469429, 48: 0.8376998404473986, 49: 0.7786950134787709, 50: 0.5835990611012452, 51: 0.03464562045881414, 52: 0.12368719530873062, 53: 0.08296549345361826, 54: 0.10564043543545532, 55: 0.2739016660817103, 56: 0.018791020075520914, 57: 0.9811929594180743, 58: 0.6490201164818314, 59: 0.6851941813811734, 60: 0.6110087711437481, 61: 0.294511546358336, 62: 0.34780834701802776, 63: 0.04090795655273638, 64: 0.391478139779456, 65: 0.9951889494670926, 66: 0.562286690168261, 67: 0.3850523842217459, 68: 0.4198849458720245, 69: 0.36420085854341, 70: 0.4097517962892635, 71: 0.5387959706739925, 72: 0.3683792606548175, 73: 0.22666649209600032, 74: 0.01080663584826147, 75: 0.04024401735519678, 76: 0.08938568369758138, 77: 0.00952297359572607, 78: 0.8214641863957417, 79: 0.5779338466222844, 80: 0.6008104661623722, 81: 0.23481887089960263, 82: 0.6032516786010461, 83: 0.8618851231210595, 84: 0.04511727345355321, 85: 0.6521956916855899, 86: 0.8558456173282006, 87: 0.27538109869668903, 88: 0.20989577777962443, 89: 0.9085100773968943, 90: 0.10874409867093993, 91: 0.46601891905327053, 92: 0.2868015606790053, 93: 0.21727828787803027, 94: 0.8997842155399634, 95: 0.30564218527533904, 96: 0.7449234241315477, 97: 0.9248024505045878, 98: 0.8727443837097717, 99: 0.22214742970595247, 100: 0.9922406080824444}, 2: {1: 0.20997273259612026, 2: 0.584524321365508, 3: 0.985043961013027, 4: 0.2095890275282868, 5: 0.295684216528073, 6: 0.15884876898586398, 7: 0.011418730789158005, 8: 0.5857025370584538, 9: 0.4159553190827414, 10: 0.4842551978402969, 11: 0.11955965669764823, 12: 0.010037660162754536, 13: 0.4921664990422667, 14: 0.5304665483250485, 15: 0.9556731617804133, 16: 0.6352910150786426, 17: 0.008584160509506056, 18: 0.8029847162102655, 19: 0.5623330171069266, 20: 0.7656785736563787, 21: 0.47801856559690525, 22: 0.4123428863513324, 23: 0.16734595328666813, 24: 0.9434498383526319, 25: 0.9304321716350199, 26: 0.00856372896301738, 27: 0.07156006994659814, 28: 0.44865665615096273, 29: 0.09723641942380379, 30: 0.7272204961995441, 31: 0.9638744946371909, 32: 0.5304072297324635, 33: 0.9995968741138684, 34: 0.5750313801351343, 35: 0.38677448872767783, 36: 0.020817821394570002, 37: 0.9303586826174137, 38: 0.6659037787637124, 39: 0.5916618406808299, 40: 0.5023392030489251, 41: 0.795403670378548, 42: 0.13511776190647018, 43: 0.7284439282193361, 44: 0.3764812367698589, 45: 0.9562566765014496, 46: 0.3750068670591665, 47: 0.9892799520888504, 48: 0.4920232728738172, 49: 0.7671576547162926, 50: 0.8950254598841172, 51: 0.18597166991137837, 52: 0.9787578782727907, 53: 0.9857394108325517, 54: 0.9817098932809507, 55: 0.6245268011361371, 56: 0.28110066511936826, 57: 0.5520139088606616, 58: 0.43875360783262485, 59: 0.7100550855287495, 60: 0.48282650173964636, 61: 0.16758648047209102, 62: 0.1774924496150463, 63: 0.7200465908566275, 64: 0.13654123836547516, 65: 0.377905040993186, 66: 0.1633909767471331, 67: 0.36954614711612355, 68: 0.5589487275425492, 69: 0.8638058659473498, 70: 0.9158649100454873, 71: 0.11090911964420391, 72: 0.9387342418904266, 73: 0.11532922447037908, 74: 0.9662764253052823, 75: 0.6890629841668177, 76: 0.7703156809092662, 77: 0.08692428969435495, 78: 0.9792365853457791, 79: 0.6024859542847157, 80: 0.2190534666383115, 81: 0.887694841108498, 82: 0.4320885911944372, 83: 0.30206352468252307, 84: 0.09489041997884651, 85: 0.3251404825245815, 86: 0.8633506392667809, 87: 0.2546100507601282, 88: 0.05318753458860881, 89: 0.3374706231944061, 90: 0.41585459523692336, 91: 0.5723253455534487, 92: 0.15932367935033576, 93: 0.5570395051127109, 94: 0.41856475365598655, 95: 0.46998026352210553, 96: 0.16424361923443886, 97: 0.4240672300506769, 98: 0.2201121350114852, 99: 0.04359736977937867, 100: 0.964119763009854}, 3: {1: 0.7510897338449862, 2: 0.9076228682735988, 3: 0.7339536244127648, 4: 0.9464750784375585, 5: 0.07811322407493482, 6: 0.7074357134534295, 7: 0.7270958311328065, 8: 0.32020612175378893, 9: 0.23288628424381308, 10: 0.6645608707281775, 11: 0.9322149281384674, 12: 0.6230112219527227, 13: 0.6624933326676258, 14: 0.36774443280572955, 15: 0.7342070284920418, 16: 0.27386867213464783, 17: 0.9496444548458465, 18: 0.38830556107649883, 19: 0.027994843387077917, 20: 0.5679866098199162, 21: 0.4985592461366243, 22: 0.3965872014884694, 23: 0.8345825165744425, 24: 0.5849978790352458, 25: 0.7387606544136373, 26: 0.9744772722677292, 27: 0.20570154945740005, 28: 0.8109158697025385, 29: 0.9641036615522637, 30: 0.7570235465288411, 31: 0.15968278202005004, 32: 0.36517044109204533, 33: 0.46255816299934616, 34: 0.023360806400089307, 35: 0.10778259522764477, 36: 0.9453434968390678, 37: 0.568050636668371, 38: 0.765592124385641, 39: 0.9288118635515084, 40: 0.13297612228231326, 41: 0.30860451572841585, 42: 0.6749907482824605, 43: 0.4624012229657496, 44: 0.07268992115850836, 45: 0.8685816597353655, 46: 0.8639376227144658, 47: 0.7204682738073552, 48: 0.10873337165797903, 49: 0.908354115016406, 50: 0.3990866858325224, 51: 0.8260605848101986, 52: 0.9763414516416431, 53: 0.9622514528355508, 54: 0.5037938177644611, 55: 0.8703254733292892, 56: 0.039430489082456166, 57: 0.3842644545052618, 58: 0.24154418932271338, 59: 0.580679383991328, 60: 0.8097722510402553, 61: 0.527458581363338, 62: 0.46980639441136307, 63: 0.16606380438847845, 64: 0.25921114609890283, 65: 0.2527042179480895, 66: 0.7730390749207451, 67: 0.5072586192032789, 68: 0.41756908006555504, 69: 0.7607038093279203, 70: 0.6931833618435526, 71: 0.2597043160186584, 72: 0.6122673538965917, 73: 0.5795637100318697, 74: 0.4244321194648828, 75: 0.8507219331505792, 76: 0.470505393013119, 77: 0.4293283199869825, 78: 0.5397426916887571, 79: 0.8455709767707915, 80: 0.7858784357896732, 81: 0.10385704452217559, 82: 0.8792384368531345, 83: 0.35045057034772353, 84: 0.7125246705349257, 85: 0.8561340445879692, 86: 0.2839727400511365, 87: 0.7689974531956655, 88: 0.6267609411148582, 89: 0.20645953484239754, 90: 0.9726501475503465, 91: 0.24546063609211222, 92: 0.04999687694136945, 93: 0.04422276188113572, 94: 0.5559765734343449, 95: 0.42083710969812815, 96: 0.7097742365268757, 97: 0.8718038749847933, 98: 0.8935062243434005, 99: 0.5980479868135594, 100: 0.07466560346365514}, 4: {1: 0.3531671559879107, 2: 0.5772010663439113, 3: 0.6670079405623853, 4: 0.6928943894423992, 5: 0.1708175624605175, 6: 0.7956960871212188, 7: 0.1617904424230403, 8: 0.0669888921568399, 9: 0.14967393018373587, 10: 0.5591403961600543, 11: 0.6511159392951653, 12: 0.8746210457469762, 13: 0.02088772667743355, 14: 0.7150055644545737, 15: 0.5826094892167554, 16: 0.07180215068082252, 17: 0.5910217056128928, 18: 0.31060884183950255, 19: 0.7871082698275077, 20: 0.2828234449999252, 21: 0.5147461989668041, 22: 0.40622916354649075, 23: 0.052254947857210854, 24: 0.44759602992625436, 25: 0.6375036116811799, 26: 0.22326247200531202, 27: 0.3766767924545916, 28: 0.7759428807985934, 29: 0.06220330914661465, 30: 0.6853608476805336, 31: 0.09341258099561911, 32: 0.8108180510585306, 33: 0.422461606327313, 34: 0.42726727806379894, 35: 0.471100622797328, 36: 0.9779424786916165, 37: 0.4259430836158107, 38: 0.2786706743430052, 39: 0.9363650035055994, 40: 0.9724018599460983, 41: 0.47633883491276807, 42: 0.48143323254759307, 43: 0.3555961101011492, 44: 0.5021065675313661, 45: 0.9177512252287102, 46: 0.3356507968616075, 47: 0.6188836797795538, 48: 0.1493231870240378, 49: 0.09848704247234086, 50: 0.5562352172538332, 51: 0.4658899788918497, 52: 0.5151898215512513, 53: 0.3698720941399224, 54: 0.40649212807544965, 55: 0.2009240584157307, 56: 0.875914364936012, 57: 0.27711070505165825, 58: 0.39713943823819475, 59: 0.37813417720935705, 60: 0.6091890189074246, 61: 0.05464785840413999, 62: 0.11211474719391856, 63: 0.3850899829565184, 64: 0.3813331555638434, 65: 0.05931567796685289, 66: 0.6193684240417944, 67: 0.2839432392955653, 68: 0.022823161698874994, 69: 0.02304937333309498, 70: 0.2031134597446136, 71: 0.6117498367965277, 72: 0.214609585545111, 73: 0.5136880218740605, 74: 0.641870427180905, 75: 0.19700143227601785, 76: 0.0735955762442545, 77: 0.2952575344408426, 78: 0.5054957424986277, 79: 0.2382534793888671, 80: 0.08201859631153474, 81: 0.5937144746089186, 82: 0.1989115692099197, 83: 0.1554712843270435, 84: 0.37548015042744287, 85: 0.9736671803459744, 86: 0.24575268581715337, 87: 0.5460431538781453, 88: 0.46540477521829593, 89: 0.7442099677479861, 90: 0.8829811096010031, 91: 0.63872025902857, 92: 0.44120775716962135, 93: 0.7284895626036668, 94: 0.06947051172114416, 95: 0.26396255698154114, 96: 0.9715295635341947, 97: 0.5721493839818677, 98: 0.23716386589416139, 99: 0.34954648597794136, 100: 0.7349689940090648}}