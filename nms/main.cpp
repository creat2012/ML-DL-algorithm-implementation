#include <iostream>
#include "nms.hpp"
using namespace std;

const int MAX = 105; // max mount bounding box

int main()
{
	vector<Bbox> bx;
	int n; // the mount will process
	cin >> n;
	cout << "begin input" << endl;
	for(int i = 0; i < n; ++ i){
		Bbox bbx;
		cin >> bbx.x >> bbx.y >> bbx.w >> bbx.h >> bbx.score;
		bx.push_back(bbx);
	}
	cout << "end input" << endl;
	NMS nms(bx, 0.5);
	nms.nms();
	return 0;
}