#include <iostream>
#include <cmath>
#include <time.h>
using namespace std;

int main(){
    // defining some constant variables
    int N = 1000, Reps = 1000;
    float J = 1.0, Temp = 0.0;

    int lattice[N][N];
    srand(time(0));

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            lattice[i][j] = rand() % 2;
            if (lattice[i][j] == 0){
                lattice[i][j] = -1;
            }
        }
    }

    int lat[N][N];

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            lat[i][j] = lattice[i][j];
        }
    }

    double beta;
    if (Temp == 0.0){
        beta = 1/Temp;
    }
    else{
        beta = numeric_limits<double>::infinity();
    }

    cout<<"\n";

    for(int k = 0; k < Reps; k++){
        int index_i = rand() % N, index_j = rand() % N;
        int index_i_minus_1 = (index_i == 0) ? N-1 : index_i-1;
        int index_j_minus_1 = (index_j == 0) ? N-1 : index_j-1;
        // debug line
        // cout << "i:" << index_i << ", j:" << index_j << ", i-1:" << index_i_minus_1 << ", j-1:" << index_j_minus_1 << ", i+1:" << (index_i+1)%N << ", j+1:" << (index_j+1)%N << "\n";
        int energy_o = J*lattice[index_i][index_j]*(lattice[(index_i+1)%N][index_j]+lattice[index_i_minus_1][index_j]+lattice[index_i][(index_j+1)%N]+lattice[index_i][index_j_minus_1]);
        if(energy_o >= -energy_o){
            lattice[index_i][index_j] *= -1;
        }
        else{
            double transition_prob = exp(-beta*abs(2*energy_o));
            float ran = (float)(rand()) / (float)(RAND_MAX);
            if(transition_prob > ran){
                lattice[index_i][index_j] *= -1;
            }
        }
    }

    cout<<"\n";

    // for(int i = 0; i < N; i++){
    //     for(int j = 0; j < N; j++){
    //         cout << lat[i][j] << "  ";
    //     }
    //     cout << "\n";
    // }

    double energy_sys_o = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int i_minus_1 = (i == 0) ? N-1 : i-1;
            int j_minus_1 = (j == 0) ? N-1 : j-1;
            energy_sys_o += J*lat[i][j]*(lat[(i+1)%N][j]+lat[i_minus_1][j]+lat[i][(j+1)%N]+lat[i][j_minus_1]);
        }
    }

    double energy_sys_p = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int i_minus_1 = (i == 0) ? N-1 : i-1;
            int j_minus_1 = (j == 0) ? N-1 : j-1;
            energy_sys_p += J*lattice[i][j]*(lattice[(i+1)%N][j]+lattice[i_minus_1][j]+lattice[i][(j+1)%N]+lattice[i][j_minus_1]);
            // debug line
            // if(i == 1){
                // cout << J*lattice[i][j]*(lattice[(i+1)%N][j]+lattice[i_minus_1][j]+lattice[i][(j+1)%N]+lattice[i][j_minus_1]) << " dry,";
            // }
        }
    }
    cout << "Initial Energy of system: " << energy_sys_o << " o \n";

    // for(int i = 0; i < N; i++){
    //     for(int j = 0; j < N; j++){
    //         cout << lattice[i][j] << "  ";
    //     }
    //     cout << "\n";
    // }
    cout << "Final Energy of system: " << energy_sys_p;
    return 0;
}