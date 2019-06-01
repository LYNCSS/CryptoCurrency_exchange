#include <stdio.h>
#include <stdlib.h>
#include "Linear_Algebra.h"
#include <math.h>

int relaxion(LN_matrix* _graph, unsigned trgt ,unsigned mid , unsigned *_predecessor, double *dist_s){ // relaxion on the distance from s to trgt by going through mid
    int flag = 0;
    if(dist_s[mid] + LN_index_dvalue(_graph, mid, trgt) < dist_s[trgt]){
        dist_s[trgt] = dist_s[mid] + LN_index_dvalue(_graph, mid, trgt);
        _predecessor[trgt] = mid;
        flag = 1;
    }
    return flag;
}

void _update_matrix(LN_matrix* _distance_matrix,unsigned _iteration, unsigned *_predecessor, double *dist_s){

    /*The Floyed-Warshall algorithm which update the distance matrix by*/

    for(unsigned _raw_iter = 0; _raw_iter < _distance_matrix -> rows; _raw_iter++){
        for(unsigned _col_index = 0; _col_index < _distance_matrix->rows; _col_index++){
            
        }
    }
}

void _record_Ncycle(unsigned *_nominees, unsigned started, unsigned *_parent){
    unsigned _tmp = _parent[started];
    unsigned index = 0;

    while(_tmp != started){
        _nominees[index] = _tmp;
        index++;
        _tmp = _parent[_tmp];
    }
}

unsigned* Detect_N_cycle(LN_matrix* _graph, unsigned start){

    /*The function return an unsigned array to represent the number of node in a cycle that shaped negative cycle. It is an implementation of Floyed-Warshall, which take O(n^3).
    _graph: is the target graph which represented in adjancy matrix, the data structure of the matrix is defined in Linear_Algebra.h
    start: the started point*/

    unsigned *nominees; //the nodes shaped a negative cycle
    LN_matrix *_distance_matrix = LN_copy_matrix(_graph);
    LN_matrix *_parent_matrix = LN_init_INF_matrix(_graph -> rows, _graph -> cols);
    

    dist_s[start] = 0.0;
    for(unsigned _iteration = 0; _iteration<(_graph->cols); _iteration++){
        
    }
    LNDECREF(_distance_matrix);
    LNDECREF(_parent_matrix);
    
}

int main(){
    LN_matrix *graph;
}