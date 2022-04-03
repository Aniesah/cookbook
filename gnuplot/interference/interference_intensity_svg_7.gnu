# Plot inteference intensity of 7 source
# (CC 2022) Sparisoma Viridi
# dudung@gmail.com
# 2022.04.03.40198

# svg output is selected
set term svg size 320,200 enhanced font "Times, 12"

# some constants
PI = 3.14159
E0 = 1
wt = PI/2

# electric field E1 - E3
E1(dq) = E0 * sin(wt + 0 * dq)
E2(dq) = E0 * sin(wt + 1 * dq)
E3(dq) = E0 * sin(wt + 2 * dq)
E4(dq) = E0 * sin(wt + 3 * dq)
E5(dq) = E0 * sin(wt + 4 * dq)
E6(dq) = E0 * sin(wt + 5 * dq)
E7(dq) = E0 * sin(wt + 6 * dq)

# resultants and intensities
Et(dq) = E1(dq) + E2(dq) + E3(dq) + E4(dq) + E5(dq) + E6(dq) \
+ E7(dq)
I(dq) = Et(dq) * Et(dq)

# axis settings
set xlabel "{/Symbol f/p}"
set ylabel "{/Italic I / I_o}"
set xrange [-4:4]
set xtics 1
set grid lw 2

# samples resolution
set samples 5000

# two sources interference
set output "interference-pattern-slit-7.svg"
set yrange [0:49]
set ytics 7
plot I(x * PI) t "" lw 2 lc rgb '#00cc00'
