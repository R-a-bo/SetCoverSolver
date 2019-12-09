from approximations import Approximations

cover = [({898, 515, 9, 907, 397, 781, 271, 529, 19, 407, 666, 542, 926, 801, 547, 164, 38, 551, 41, 682, 427, 556, 813, 942, 304, 309, 950, 58, 572, 63, 839, 584, 200, 202, 844, 205, 975, 337, 849, 468, 85, 864, 225, 866, 237, 505, 623, 625, 499, 244, 502, 377, 124, 893, 254}, 4)]

subset_tuples = [({898, 515, 9, 907, 397, 781, 271, 529, 19, 407, 666, 542, 926, 801, 547, 164, 38, 551, 41, 682, 427, 556, 813, 942, 304, 309, 950, 58, 572, 63, 839, 584, 200, 202, 844, 205, 975, 337, 849, 468, 85, 864, 225, 866, 237, 505, 623, 625, 499, 244, 502, 377, 124, 893, 254}, 4), ({515, 773, 907, 397, 526, 529, 533, 407, 664, 540, 542, 164, 38, 551, 554, 427, 813, 942, 817, 50, 309, 957, 202, 842, 975, 976, 720, 468, 854, 859, 221, 864, 225, 618, 625, 499, 117, 890}, 12), ({898, 515, 900, 773, 10, 397, 529, 785, 535, 664, 407, 666, 540, 541, 542, 926, 801, 547, 164, 38, 551, 41, 554, 682, 556, 813, 430, 942, 304, 427, 50, 309, 950, 184, 441, 572, 957, 190, 839, 200, 202, 842, 844, 975, 720, 337, 208, 85, 854, 987, 732, 859, 221, 92, 864, 480, 225, 866, 618, 237, 505, 623, 627, 499, 244, 502, 761, 890, 124, 893, 254}, 19), ({898, 515, 900, 773, 134, 9, 907, 781, 526, 397, 271, 785, 533, 666, 540, 541, 926, 164, 677, 38, 551, 41, 682, 427, 430, 304, 184, 58, 187, 572, 190, 63, 710, 839, 200, 584, 842, 202, 205, 975, 208, 849, 854, 859, 732, 221, 92, 480, 225, 618, 623, 625, 627, 499, 761, 117, 631, 377, 890, 124, 893, 254}, 19), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 682, 184, 187, 190, 710, 200, 202, 205, 208, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 801, 813, 304, 817, 309, 839, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 950, 441, 957, 975, 976, 468, 987, 480, 499, 502, 505}, 20), ({9, 10, 237, 623, 50, 533, 184, 254}, 21), ({898, 515, 900, 773, 394, 907, 10, 781, 526, 271, 529, 19, 535, 664, 407, 540, 541, 926, 164, 38, 551, 41, 554, 682, 427, 813, 50, 950, 441, 58, 187, 572, 957, 446, 63, 190, 710, 839, 200, 205, 975, 337, 849, 85, 987, 92, 221, 732, 859, 864, 225, 866, 480, 377, 618, 505, 237, 625, 499, 244, 117, 502, 631, 627, 761, 124, 893, 254}, 22), ({134, 9, 10, 397, 526, 781, 529, 19, 533, 407, 540, 542, 547, 551, 41, 554, 427, 682, 813, 304, 50, 184, 572, 957, 446, 190, 63, 839, 584, 200, 202, 205, 208, 85, 732, 480, 225, 864, 866, 618, 237, 627, 244, 761, 502, 377, 124}, 23), ({480, 710, 200, 907, 237, 623, 849, 50, 817, 502, 890, 893, 63}, 26), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 208, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 801, 813, 309, 839, 842, 844, 849, 337, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 33), ({515, 900, 134, 394, 907, 10, 397, 526, 271, 529, 785, 533, 535, 664, 407, 666, 540, 541, 926, 801, 547, 164, 677, 38, 551, 41, 554, 682, 813, 430, 304, 817, 50, 309, 950, 184, 441, 58, 187, 957, 190, 710, 584, 200, 202, 842, 844, 205, 975, 208, 337, 720, 849, 468, 85, 854, 987, 732, 859, 221, 480, 864, 866, 618, 505, 237, 623, 625, 499, 244, 117, 502, 631, 761, 377, 890, 124, 893, 254}, 34), ({898, 515, 773, 134, 9, 394, 907, 10, 781, 526, 397, 785, 529, 19, 533, 535, 664, 666, 540, 541, 926, 801, 164, 677, 38, 551, 41, 554, 682, 556, 813, 942, 430, 817, 309, 184, 58, 187, 572, 957, 446, 190, 63, 839, 584, 200, 842, 202, 844, 205, 975, 720, 849, 208, 976, 337, 854, 859, 987, 221, 92, 480, 864, 866, 225, 377, 618, 237, 623, 625, 627, 499, 117, 502, 631, 244, 761, 890, 124, 893, 254}, 38), ({898, 515, 900, 134, 9, 394, 907, 397, 781, 785, 529, 19, 533, 535, 407, 664, 666, 540, 541, 926, 542, 801, 164, 677, 38, 551, 41, 556, 813, 430, 942, 304, 50, 950, 184, 441, 58, 187, 572, 957, 446, 63, 710, 839, 584, 200, 844, 208, 849, 720, 976, 337, 85, 854, 987, 859, 92, 221, 480, 225, 866, 377, 618, 237, 623, 627, 499, 761, 502, 244, 117, 505, 890, 124, 893}, 38), ({900, 773, 9, 10, 394, 785, 533, 926, 542, 547, 164, 551, 682, 813, 942, 817, 309, 950, 184, 441, 58, 957, 584, 202, 844, 205, 849, 85, 859, 92, 480, 225, 623, 627, 499, 244, 502, 761, 893}, 40), ({898, 515, 900, 134, 394, 10, 397, 271, 785, 529, 407, 664, 666, 540, 542, 801, 547, 164, 677, 41, 554, 427, 556, 813, 942, 682, 304, 817, 309, 441, 58, 187, 572, 957, 190, 446, 63, 710, 839, 200, 584, 202, 844, 205, 975, 208, 849, 337, 720, 468, 854, 987, 92, 859, 732, 866, 631, 377, 505, 237, 623, 627, 244, 499, 117, 502, 761, 890, 124}, 41), ({202, 859, 540}, 41), ({515, 773, 134, 10, 394, 907, 271, 529, 785, 19, 535, 540, 541, 926, 542, 801, 547, 38, 551, 682, 427, 556, 942, 430, 50, 184, 441, 58, 187, 572, 446, 710, 584, 202, 842, 844, 205, 975, 720, 208, 849, 468, 85, 854, 859, 732, 864, 225, 866, 618, 237, 625, 627, 502, 631, 505, 890, 893, 254}, 42), ({515, 9, 526, 529, 19, 533, 535, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 184, 187, 190, 710, 200, 202, 205, 208, 720, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 394, 907, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 43), ({515, 9, 10, 526, 529, 19, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 208, 720, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 849, 337, 854, 859, 864, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 44), ({515, 677, 907, 50, 627, 117, 58, 221}, 48), ({898, 900, 781, 397, 271, 785, 529, 19, 533, 666, 540, 542, 926, 801, 547, 38, 551, 682, 554, 942, 430, 50, 950, 184, 187, 63, 710, 839, 584, 202, 842, 844, 208, 337, 468, 854, 859, 221, 864, 618, 627, 502, 631, 377}, 48), ({225, 801, 164, 710, 682, 907, 942, 975, 976, 720, 854, 441, 58, 541, 890}, 49), ({547, 515, 9, 554, 394, 682, 942, 976, 337, 190, 893, 926}, 51), ({898, 900, 907, 785, 533, 664, 540, 926, 551, 41, 556, 813, 304, 817, 50, 441, 187, 190, 710, 200, 202, 844, 205, 208, 85, 854, 987, 237, 623, 502, 631, 505, 890, 254}, 52), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 208, 720, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 52), ({898, 515, 900, 773, 134, 9, 394, 781, 526, 271, 397, 785, 19, 533, 535, 407, 664, 666, 540, 926, 542, 801, 547, 677, 38, 551, 41, 682, 427, 556, 813, 430, 304, 50, 184, 58, 187, 957, 190, 710, 839, 584, 200, 842, 844, 205, 975, 976, 208, 720, 337, 468, 85, 854, 859, 92, 221, 732, 987, 480, 864, 866, 377, 618, 237, 623, 625, 499, 117, 502, 631, 505, 890, 124, 893, 254}, 54), ({515, 900, 9, 394, 907, 10, 397, 529, 19, 533, 666, 926, 547, 38, 551, 554, 427, 556, 813, 942, 304, 184, 441, 572, 957, 446, 710, 839, 584, 842, 202, 844, 975, 976, 337, 849, 854, 859, 732, 221, 92, 864, 225, 618, 623, 625, 244, 761, 505, 890, 124, 254}, 57), ({898, 773, 9, 394, 907, 10, 397, 526, 271, 781, 785, 19, 664, 540, 542, 801, 164, 677, 38, 551, 41, 682, 427, 556, 942, 817, 309, 950, 184, 441, 187, 572, 957, 446, 710, 584, 200, 202, 842, 844, 975, 976, 337, 208, 849, 85, 854, 859, 732, 92, 221, 987, 864, 225, 480, 618, 505, 623, 625, 499, 244, 117, 761, 631, 377, 890, 124, 893, 254}, 61), ({900, 773, 9, 10, 397, 271, 529, 785, 19, 533, 535, 541, 542, 801, 547, 164, 677, 551, 41, 554, 682, 427, 813, 556, 304, 950, 441, 58, 187, 572, 957, 190, 446, 839, 842, 975, 976, 849, 859, 92, 866, 377, 618, 505, 623, 625, 627, 244, 631, 761, 124, 893}, 62), ({900, 773, 9, 394, 907, 397, 271, 529, 19, 533, 407, 535, 664, 540, 926, 801, 547, 164, 677, 41, 554, 427, 682, 430, 817, 309, 950, 184, 441, 58, 187, 957, 190, 63, 446, 710, 584, 202, 844, 975, 720, 208, 337, 849, 854, 859, 732, 987, 92, 480, 864, 866, 377, 618, 237, 623, 627, 244, 117, 761, 631, 505, 890, 893}, 64), ({898, 515, 900, 773, 10, 907, 394, 397, 785, 19, 533, 407, 540, 541, 801, 547, 164, 38, 551, 41, 554, 427, 556, 813, 942, 430, 304, 682, 50, 309, 950, 184, 957, 446, 63, 710, 584, 842, 205, 975, 976, 849, 85, 854, 859, 732, 225, 866, 377, 618, 237, 627, 499, 117, 631, 761, 890, 124, 893, 254}, 68), ({898, 515, 900, 773, 134, 9, 10, 907, 394, 781, 526, 271, 529, 785, 19, 533, 535, 666, 540, 541, 542, 926, 547, 164, 38, 551, 41, 682, 427, 554, 813, 942, 430, 556, 817, 50, 309, 950, 184, 441, 58, 187, 572, 957, 446, 63, 190, 710, 839, 584, 200, 202, 975, 976, 337, 849, 208, 468, 85, 854, 720, 987, 859, 92, 732, 221, 864, 225, 866, 480, 618, 505, 237, 623, 499, 117, 502, 631, 761, 377, 890, 124, 893, 254}, 68), ({515, 900, 773, 134, 9, 10, 394, 907, 781, 526, 271, 529, 785, 19, 533, 535, 664, 407, 666, 540, 541, 801, 547, 677, 38, 551, 41, 682, 427, 556, 554, 942, 430, 304, 817, 50, 309, 184, 441, 58, 187, 957, 710, 839, 200, 842, 202, 975, 976, 208, 720, 337, 468, 85, 859, 732, 987, 92, 864, 225, 866, 480, 237, 625, 627, 244, 499, 502, 631, 761, 890, 124, 893, 254}, 69), ({898, 515, 134, 9, 394, 10, 781, 529, 19, 535, 664, 540, 926, 801, 547, 164, 677, 38, 551, 554, 682, 556, 813, 430, 942, 304, 817, 50, 309, 950, 184, 441, 58, 187, 572, 957, 190, 446, 63, 710, 839, 584, 200, 842, 208, 720, 337, 849, 468, 85, 987, 732, 859, 221, 92, 480, 864, 225, 237, 623, 499, 627, 117, 631, 505, 893}, 71), ({515, 900, 773, 397, 526, 271, 529, 533, 535, 407, 540, 801, 547, 164, 551, 41, 554, 430, 304, 817, 950, 184, 58, 190, 63, 446, 200, 584, 202, 842, 205, 720, 337, 468, 85, 854, 987, 859, 864, 866, 618, 625, 627, 244, 117, 502, 499, 505, 124, 254}, 72), ({9, 10, 526, 19, 533, 535, 541, 542, 547, 38, 551, 41, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 208, 720, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 377, 893, 898, 394, 907, 397, 407, 926, 427, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 505}, 73), ({134, 551, 942, 19, 987}, 75), ({898, 515, 773, 394, 781, 271, 533, 407, 666, 540, 541, 542, 926, 38, 41, 304, 817, 184, 446, 584, 200, 202, 975, 976, 849, 854, 866, 618, 237, 505, 124}, 75), ({505, 907, 761}, 76), ({515, 900, 773, 134, 9, 10, 907, 394, 397, 781, 526, 529, 785, 19, 533, 407, 664, 535, 666, 540, 541, 926, 542, 801, 547, 164, 677, 38, 551, 41, 682, 554, 427, 813, 942, 430, 304, 817, 50, 556, 309, 950, 184, 441, 187, 572, 446, 63, 190, 710, 584, 200, 202, 842, 844, 975, 208, 720, 849, 337, 976, 85, 854, 987, 92, 221, 859, 864, 225, 866, 480, 237, 623, 625, 499, 627, 117, 502, 631, 244, 377, 124, 893, 254}, 77), ({898, 515, 773, 134, 9, 394, 10, 397, 781, 785, 529, 533, 407, 535, 664, 666, 540, 541, 542, 926, 801, 547, 164, 677, 551, 41, 554, 682, 556, 813, 304, 50, 309, 950, 187, 572, 957, 446, 63, 710, 839, 200, 202, 205, 975, 976, 337, 849, 208, 854, 987, 732, 221, 859, 864, 225, 866, 618, 505, 625, 499, 117, 761, 377, 124, 254}, 79), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 208, 720, 732, 221, 225, 237, 244, 761, 254, 773, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 430, 942, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 79), ({515, 900, 9, 394, 10, 397, 271, 529, 785, 19, 533, 535, 407, 666, 540, 541, 542, 926, 801, 547, 164, 677, 38, 554, 682, 556, 813, 430, 942, 304, 50, 950, 184, 441, 58, 187, 957, 190, 63, 839, 200, 584, 202, 975, 720, 337, 208, 468, 85, 859, 987, 864, 225, 866, 480, 631, 377, 618, 623, 625, 499, 627, 761, 502, 244, 505, 890, 893}, 80), ({898, 773, 10, 394, 907, 781, 526, 533, 664, 926, 542, 801, 547, 164, 677, 551, 41, 682, 427, 556, 942, 430, 304, 50, 309, 950, 190, 446, 710, 839, 584, 842, 202, 205, 975, 976, 720, 337, 208, 468, 85, 854, 859, 732, 92, 221, 866, 618, 237, 623, 499, 761, 117, 377}, 81), ({710, 526}, 81), ({898, 515, 900, 773, 134, 9, 10, 781, 271, 785, 529, 533, 664, 541, 926, 547, 164, 677, 554, 427, 556, 430, 942, 817, 309, 950, 441, 58, 187, 572, 446, 190, 584, 202, 844, 849, 85, 859, 221, 864, 618, 237, 499, 244, 505, 890, 893, 254}, 83), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 237, 244, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 84), ({9, 10, 526, 529, 19, 533, 535, 540, 541, 547, 38, 551, 41, 554, 556, 50, 58, 572, 584, 85, 92, 618, 623, 625, 117, 124, 134, 664, 666, 164, 682, 184, 187, 190, 710, 202, 205, 720, 208, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 849, 337, 854, 859, 864, 866, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 84), ({898, 515, 900, 9, 394, 907, 10, 397, 271, 19, 533, 407, 664, 535, 666, 540, 542, 801, 547, 164, 677, 38, 551, 41, 554, 556, 813, 942, 430, 304, 950, 184, 58, 187, 572, 957, 446, 710, 839, 584, 200, 202, 205, 720, 208, 976, 849, 468, 854, 732, 221, 92, 480, 864, 866, 225, 377, 618, 237, 627, 244, 499, 502, 117, 761, 890, 124, 893, 254}, 84), ({864, 900, 677, 682, 394, 237, 893, 813, 19, 468, 533, 502, 407, 184, 505, 957, 446, 63}, 87), ({864, 377, 202, 502}, 88), ({898, 515, 900, 773, 134, 9, 394, 10, 397, 526, 271, 781, 529, 785, 19, 533, 407, 664, 535, 666, 540, 541, 926, 542, 164, 677, 551, 41, 682, 554, 556, 813, 427, 430, 304, 817, 50, 309, 184, 441, 58, 187, 572, 957, 446, 63, 190, 710, 584, 200, 202, 842, 844, 205, 975, 208, 976, 337, 849, 468, 85, 854, 720, 859, 92, 732, 864, 866, 618, 237, 623, 627, 244, 117, 502, 631, 761, 505, 890, 499, 124, 893, 254}, 88), ({898, 773, 394, 10, 781, 526, 785, 19, 533, 664, 666, 542, 926, 801, 547, 677, 38, 551, 41, 682, 556, 942, 430, 817, 184, 441, 63, 710, 839, 584, 200, 202, 842, 844, 205, 975, 720, 976, 849, 468, 854, 859, 732, 221, 225, 866, 618, 237, 623, 625, 499, 244, 117, 502, 377, 890, 124, 893, 254}, 89), ({515, 900, 773, 9, 397, 271, 785, 529, 19, 407, 666, 540, 926, 542, 801, 677, 551, 41, 682, 817, 184, 441, 63, 710, 205, 975, 720, 208, 732, 92, 864, 225, 866, 237, 623, 627, 502, 505, 890, 893, 254}, 89), ({515, 773, 134, 9, 10, 394, 907, 397, 526, 781, 271, 529, 785, 19, 533, 407, 664, 535, 666, 540, 541, 542, 926, 801, 164, 677, 38, 551, 41, 682, 427, 554, 556, 430, 942, 813, 817, 50, 309, 950, 184, 58, 572, 957, 190, 446, 63, 710, 839, 584, 200, 202, 842, 844, 205, 976, 337, 208, 720, 468, 85, 854, 987, 92, 221, 480, 225, 866, 864, 618, 237, 623, 625, 499, 244, 761, 502, 505, 890, 124, 893}, 89), ({898, 900, 773, 9, 394, 10, 907, 526, 529, 785, 19, 533, 535, 666, 540, 541, 542, 926, 547, 677, 41, 554, 427, 682, 813, 430, 950, 184, 441, 187, 957, 190, 446, 710, 839, 200, 584, 202, 844, 205, 208, 468, 85, 859, 987, 732, 480, 237, 623, 625, 627, 761, 502, 631, 505, 890, 124, 893, 254}, 90), ({773, 551, 839, 9, 10, 556, 237, 942, 623, 124, 849, 50, 304, 627, 407, 666, 572, 446}, 90), ({773, 134, 10, 781, 397, 271, 19, 407, 535, 540, 926, 551, 41, 682, 813, 430, 441, 187, 446, 710, 584, 842, 844, 205, 975, 976, 208, 720, 468, 854, 92, 225, 623, 117, 505, 890, 124, 893}, 91), ({898, 515, 773, 134, 9, 394, 10, 907, 781, 397, 526, 785, 19, 407, 535, 666, 540, 541, 926, 542, 801, 547, 164, 677, 38, 551, 41, 554, 427, 813, 430, 942, 817, 950, 184, 58, 187, 572, 957, 190, 63, 710, 839, 200, 584, 202, 842, 844, 205, 975, 976, 208, 468, 85, 854, 859, 987, 221, 92, 732, 864, 480, 866, 225, 377, 618, 237, 623, 625, 627, 499, 117, 502, 244, 505, 890, 124, 893, 254}, 93), ({898, 515, 397, 781, 785, 535, 541, 926, 542, 38, 41, 682, 942, 950, 187, 572, 710, 200, 202, 205, 975, 85, 854, 859, 732, 987, 618, 237, 244, 124, 254}, 94), ({10, 50, 631, 664, 190}, 95), ({781, 208, 407, 540, 893, 254, 63}, 95), ({515, 900, 773, 9, 394, 19, 533, 535, 926, 677, 551, 430, 942, 309, 950, 441, 187, 190, 839, 584, 849, 85, 866, 237, 623, 499, 117, 502, 377}, 96), ({898, 515, 773, 9, 907, 397, 526, 271, 781, 529, 19, 533, 407, 664, 535, 666, 541, 542, 926, 801, 547, 164, 38, 551, 41, 682, 554, 556, 430, 942, 304, 817, 50, 309, 950, 184, 441, 58, 572, 957, 446, 710, 839, 584, 200, 842, 202, 844, 205, 975, 208, 337, 720, 468, 85, 854, 859, 732, 221, 92, 987, 480, 866, 237, 505, 623, 625, 627, 499, 244, 761, 631, 502, 377, 890, 124, 893}, 98), ({515, 900, 394, 397, 271, 533, 407, 540, 541, 926, 38, 551, 41, 427, 556, 813, 430, 304, 817, 50, 309, 190, 446, 63, 710, 839, 844, 720, 337, 85, 732, 480, 866, 627, 631, 890, 893}, 102), ({898, 515, 773, 10, 907, 781, 271, 785, 19, 407, 664, 535, 666, 541, 926, 801, 547, 164, 677, 41, 554, 682, 430, 304, 817, 950, 184, 441, 58, 572, 957, 190, 446, 710, 839, 584, 202, 844, 975, 208, 337, 720, 976, 468, 85, 854, 987, 92, 221, 859, 480, 866, 618, 237, 505, 623, 499, 244, 117, 631, 377, 254}, 103), ({898, 515, 900, 134, 9, 10, 394, 907, 397, 526, 785, 529, 19, 533, 535, 664, 666, 541, 926, 542, 801, 547, 164, 677, 38, 551, 41, 682, 554, 556, 427, 430, 942, 817, 50, 950, 187, 572, 957, 190, 446, 63, 839, 200, 584, 842, 202, 844, 205, 975, 976, 849, 208, 720, 85, 854, 859, 92, 987, 732, 221, 864, 480, 866, 377, 618, 237, 623, 625, 627, 244, 117, 502, 631, 761, 505, 890, 124, 893, 254}, 103), ({898, 515, 900, 773, 134, 9, 10, 907, 394, 397, 781, 271, 526, 529, 785, 19, 533, 535, 664, 407, 666, 540, 926, 801, 547, 164, 677, 38, 551, 41, 554, 427, 556, 813, 942, 430, 304, 817, 50, 309, 950, 441, 58, 187, 572, 957, 446, 63, 710, 839, 584, 842, 844, 205, 975, 976, 337, 849, 720, 468, 85, 859, 732, 987, 221, 480, 225, 866, 377, 618, 623, 625, 627, 244, 761, 502, 631, 505, 890, 124, 254}, 105), ({898, 515, 900, 773, 134, 9, 10, 394, 397, 526, 271, 529, 785, 19, 533, 535, 664, 407, 666, 540, 926, 801, 164, 677, 38, 551, 41, 682, 556, 813, 304, 817, 50, 309, 950, 187, 572, 446, 63, 710, 200, 584, 202, 842, 844, 205, 975, 208, 976, 337, 987, 732, 221, 859, 864, 225, 866, 480, 618, 505, 627, 117, 502, 761, 890, 124, 254}, 106), ({898, 515, 773, 134, 9, 394, 907, 781, 397, 785, 529, 19, 533, 535, 664, 407, 666, 540, 541, 542, 926, 547, 164, 677, 38, 551, 41, 554, 682, 427, 556, 942, 430, 304, 950, 184, 441, 58, 187, 572, 957, 190, 446, 63, 710, 839, 200, 584, 842, 202, 844, 205, 975, 720, 208, 849, 976, 468, 337, 854, 85, 987, 92, 221, 864, 225, 866, 377, 618, 237, 623, 625, 499, 627, 117, 761, 631, 244, 505, 890, 124, 893, 254}, 107), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 710, 200, 202, 205, 720, 208, 732, 221, 225, 237, 244, 761, 254, 773, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 849, 337, 854, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 109), ({900, 134, 781, 535, 664, 677, 682, 430, 942, 446, 63, 710, 839, 202, 208, 849, 337, 468, 85, 854, 618, 499, 244, 117}, 110), ({515, 900, 773, 9, 394, 10, 397, 526, 529, 785, 19, 533, 407, 664, 540, 541, 926, 547, 38, 551, 427, 556, 813, 942, 430, 304, 817, 50, 309, 58, 187, 957, 190, 63, 710, 839, 584, 200, 842, 202, 844, 975, 976, 337, 720, 208, 468, 85, 987, 732, 859, 221, 480, 866, 377, 618, 505, 237, 625, 627, 499, 117, 502, 631, 761, 890, 893}, 111), ({85}, 112), ({898, 515, 134, 9, 10, 397, 271, 785, 533, 407, 666, 540, 541, 926, 542, 801, 547, 164, 677, 38, 551, 554, 427, 813, 430, 304, 309, 950, 184, 58, 572, 957, 63, 839, 584, 200, 842, 202, 844, 720, 337, 849, 976, 208, 85, 987, 732, 221, 92, 859, 864, 225, 480, 237, 505, 499, 627, 117, 244, 631, 377, 890, 893}, 114), ({864, 41, 10, 554, 205, 526, 813, 85, 535, 666, 124, 957, 572, 63}, 114), ({394, 907, 526, 271, 785, 407, 535, 540, 926, 542, 164, 41, 187, 572, 446, 63, 200, 202, 844, 720, 337, 92, 225, 625, 117, 502, 761, 124}, 116), ({898, 515, 773, 134, 9, 394, 907, 10, 781, 526, 271, 397, 785, 19, 533, 535, 664, 540, 541, 926, 801, 547, 677, 38, 551, 41, 682, 427, 554, 813, 430, 942, 50, 309, 184, 441, 58, 187, 572, 957, 446, 63, 190, 710, 839, 584, 200, 202, 844, 205, 975, 720, 208, 849, 976, 468, 85, 854, 337, 859, 732, 221, 92, 480, 225, 866, 864, 377, 237, 623, 625, 499, 627, 117, 502, 631, 244, 761, 890, 124, 893, 254}, 117), ({900, 773, 9, 785, 533, 535, 407, 666, 541, 542, 801, 677, 38, 554, 556, 813, 942, 304, 817, 50, 309, 950, 184, 58, 187, 572, 446, 63, 710, 839, 202, 844, 205, 976, 208, 337, 468, 85, 854, 987, 859, 480, 225, 866, 864, 618, 237, 625, 502, 377, 890, 124, 893, 254}, 118), ({515, 9, 10, 526, 529, 19, 533, 535, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 842, 844, 849, 337, 854, 859, 864, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 118), ({397, 271, 785, 407, 535, 664, 541, 926, 677, 551, 554, 950, 441, 187, 957, 200, 842, 337, 849, 854, 859, 732, 221, 244, 117, 502, 761, 377, 890}, 123), ({898, 515, 900, 773, 9, 10, 781, 526, 785, 529, 407, 664, 535, 666, 540, 542, 801, 164, 677, 551, 682, 427, 556, 813, 942, 430, 304, 817, 50, 309, 950, 441, 187, 572, 957, 446, 839, 584, 200, 202, 842, 844, 205, 975, 720, 337, 208, 468, 85, 854, 987, 859, 221, 864, 480, 377, 237, 623, 625, 499, 117, 502, 631, 761, 124, 893, 254}, 124), ({898, 900, 773, 134, 9, 394, 397, 271, 785, 529, 19, 533, 664, 540, 541, 801, 547, 554, 682, 813, 430, 304, 50, 950, 187, 957, 190, 63, 839, 200, 584, 202, 842, 844, 975, 976, 337, 720, 849, 468, 859, 92, 221, 987, 732, 480, 864, 237, 625, 499, 627, 502, 761, 890, 124, 893, 254}, 125), ({134, 394, 907, 10, 785, 664, 541, 682, 427, 184, 710, 208, 854, 987, 859, 92, 480, 225, 627, 499, 117, 761, 890}, 130), ({898, 515, 900, 134, 9, 10, 907, 394, 397, 526, 781, 785, 19, 533, 535, 664, 407, 666, 542, 547, 164, 38, 41, 554, 556, 942, 950, 184, 58, 187, 572, 190, 63, 710, 839, 200, 842, 202, 205, 975, 208, 849, 720, 976, 468, 85, 337, 859, 732, 221, 864, 480, 866, 225, 377, 618, 237, 623, 625, 499, 244, 117, 505, 890, 124, 893, 254}, 130), ({515, 900, 773, 134, 907, 781, 397, 271, 526, 529, 19, 533, 535, 664, 666, 540, 541, 926, 801, 164, 677, 551, 41, 682, 427, 556, 942, 430, 304, 817, 50, 309, 950, 184, 58, 187, 572, 957, 190, 63, 710, 839, 200, 842, 844, 976, 337, 85, 859, 732, 480, 225, 866, 618, 623, 244, 631, 505, 890, 254}, 132), ({801, 515, 773, 9, 907, 975, 623, 468, 950, 890, 92}, 133), ({898, 900, 773, 134, 9, 10, 907, 394, 781, 397, 271, 526, 529, 785, 19, 533, 535, 664, 666, 540, 542, 926, 547, 38, 551, 41, 554, 427, 556, 813, 942, 682, 304, 50, 309, 184, 441, 58, 187, 572, 957, 446, 63, 710, 839, 584, 200, 202, 842, 844, 205, 975, 976, 337, 849, 208, 468, 85, 854, 720, 987, 859, 221, 92, 732, 480, 225, 866, 864, 377, 618, 237, 623, 627, 499, 117, 502, 631, 505, 890, 124, 893, 254}, 134), ({900, 271, 785, 19, 533, 535, 541, 926, 38, 551, 554, 682, 942, 430, 950, 200, 842, 92, 225, 618, 623, 627, 244, 502, 631, 893}, 136), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 85, 92, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 900, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 505}, 143), ({515, 134, 271, 785, 535, 407, 541, 547, 677, 41, 554, 427, 556, 942, 304, 950, 184, 187, 957, 190, 63, 205, 975, 976, 337, 208, 468, 85, 859, 92, 864, 480, 225, 618, 237, 623, 499, 117, 502, 631, 893}, 144), ({785, 817}, 145), ({898, 515, 900, 773, 134, 9, 394, 907, 10, 397, 526, 271, 529, 785, 19, 533, 407, 535, 540, 541, 926, 542, 164, 38, 551, 41, 682, 427, 556, 813, 942, 304, 50, 309, 950, 184, 441, 58, 572, 957, 446, 63, 710, 839, 584, 202, 842, 844, 205, 975, 720, 849, 208, 976, 337, 85, 854, 859, 92, 221, 987, 732, 864, 225, 866, 377, 237, 623, 625, 499, 627, 117, 502, 244, 761, 505, 890, 124, 893, 254}, 147), ({773, 134, 682, 397, 533, 950, 85, 190}, 147), ({773, 134, 10, 907, 526, 540, 541, 542, 926, 38, 41, 427, 813, 817, 950, 446, 63, 200, 844, 337, 85, 854, 987, 623, 627, 244, 761, 505, 124, 893}, 152), ({801, 38, 41, 10, 682, 842, 813, 526, 785, 854, 407, 184, 190, 926}, 152), ({898, 781, 397, 975, 502, 732}, 156), ({10, 781, 397, 526, 19, 407, 535, 664, 666, 542, 926, 38, 554, 427, 942, 304, 817, 309, 950, 187, 572, 957, 839, 584, 842, 975, 976, 337, 849, 468, 854, 859, 92, 732, 987, 480, 225, 866, 377, 237, 627, 244, 631, 761, 890}, 156), ({900, 134, 9, 907, 781, 533, 664, 540, 542, 801, 551, 554, 427, 682, 50, 309, 950, 184, 187, 446, 63, 710, 839, 842, 844, 849, 854, 987, 92, 480, 618, 505, 623, 499, 244, 631, 761, 254}, 157), ({407, 801, 225, 446, 618, 556, 623, 529, 625, 540, 117, 309, 533, 505, 859, 190, 541, 926}, 160), ({515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 41, 554, 556, 50, 58, 572, 584, 85, 92, 618, 623, 625, 627, 117, 124, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 225, 237, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 427, 430, 950, 957, 975, 976, 468, 987, 480, 499, 505}, 161), ({547, 987, 202, 237, 854, 666, 859, 541, 446}, 161), ({773, 710, 551, 41, 9, 85, 533, 732, 254, 63}, 161), ({480, 773, 394, 618, 813, 942, 627, 377, 987}, 162), ({900, 10, 535, 666, 541, 677, 38, 554, 427, 813, 942, 50, 950, 957, 446, 584, 844, 205, 987, 92, 221, 618, 625, 627, 117, 890, 124, 893, 254}, 163), ({898, 900, 9, 907, 781, 397, 271, 785, 529, 19, 533, 407, 664, 541, 551, 554, 427, 556, 304, 817, 50, 309, 950, 184, 441, 187, 572, 957, 190, 446, 839, 200, 842, 202, 844, 205, 975, 720, 849, 337, 85, 854, 859, 732, 92, 225, 866, 623, 625, 761, 502, 631, 377, 890, 893}, 164), ({898, 134, 394, 907, 10, 397, 781, 529, 19, 533, 407, 664, 666, 540, 926, 542, 547, 38, 551, 41, 554, 556, 304, 817, 950, 441, 58, 187, 572, 957, 446, 63, 710, 839, 200, 584, 202, 844, 975, 208, 849, 337, 85, 859, 92, 221, 866, 618, 237, 505, 499, 244, 761, 627, 502, 377, 124, 893, 254}, 165), ({898, 134, 9, 10, 781, 785, 19, 533, 541, 926, 547, 41, 554, 813, 430, 942, 309, 184, 441, 572, 957, 584, 205, 976, 987, 732, 221, 480, 623, 625, 244, 761, 117, 377}, 165), ({898, 900, 134, 9, 10, 907, 394, 397, 781, 271, 526, 785, 529, 19, 533, 535, 407, 540, 541, 926, 801, 547, 164, 677, 551, 41, 682, 427, 430, 50, 309, 184, 58, 187, 572, 957, 446, 710, 839, 842, 975, 208, 337, 849, 720, 468, 85, 854, 976, 859, 732, 92, 987, 480, 225, 618, 237, 625, 499, 244, 117, 502, 631, 505, 890, 254}, 165), ({900, 839, 842, 907, 720, 950, 631, 221}, 167), ({515, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 225, 237, 244, 761, 254, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 337, 849, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}, 168), ({515, 900, 907, 533, 547, 38, 942, 430, 309, 572, 710, 839, 842, 202, 720, 337, 85, 854, 859, 618, 237, 627, 499, 631, 761, 890, 124, 893}, 169), ({515, 732, 677, 38, 710, 134, 773, 842, 10, 430, 975, 271, 627, 950, 540, 541}, 169)]

universe = {515, 9, 10, 526, 529, 19, 533, 535, 540, 541, 542, 547, 38, 551, 41, 554, 556, 50, 58, 572, 63, 584, 85, 92, 618, 623, 625, 627, 117, 631, 124, 134, 664, 666, 164, 677, 682, 184, 187, 190, 710, 200, 202, 205, 720, 208, 732, 221, 225, 237, 244, 761, 254, 773, 781, 271, 785, 801, 813, 304, 817, 309, 839, 842, 844, 849, 337, 854, 859, 864, 866, 377, 890, 893, 898, 900, 394, 907, 397, 407, 926, 427, 942, 430, 950, 441, 957, 446, 975, 976, 468, 987, 480, 499, 502, 505}



"""elements = set()
for subset in cover:
    for element in subset[0]:
        elements.add(element)
print(universe - elements)"""

app = Approximations(universe, subset_tuples)
#print(app.dual_rounding())
print(app.integer_program()[1], app.best())
