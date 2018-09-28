#include <iostream>
#include <stdio.h>
#include "nms.hpp"
using namespace std;


int main(int argc, char* argv[])
{
	FILE* data_file = fopen("./box.txt", "r");
	vector<Bbox> bx;
	int n; // the mount will process
	cin >> n;
	cout << "begin input" << endl;
	for(int i = 0; i < n; ++ i){
		Bbox bbx;
		//cin >> bbx.x >> bbx.y >> bbx.w >> bbx.h >> bbx.score;
		fscanf(data_file, "%lf %lf %lf %lf %lf", &bbx.x, &bbx.y, &bbx.w, &bbx.h, &bbx.score);
		bx.push_back(bbx);
	}
	cout << "end input" << endl;
	NMS nms(bx, 0.8);
	vector<Bbox> res = nms.nms();
	cout << "num :" << res.size() << endl;
	for(int i = 0; i < res.size(); ++i){
		cout << res[i].x << " " << res[i].y << " " << res[i].w << " " << res[i].h << " " << res[i].score << endl;
	}
	return 0;
}