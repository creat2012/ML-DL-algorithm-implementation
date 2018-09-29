#include <iostream>
#include <stdio.h>
#include "nms.hpp"
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace std;
using namespace cv;
void box_show(vector<Bbox> rec)
{
	Mat wboard(1000, 1000, CV_8UC3);
	//cout << wboard.row << " " << wboard.col << endl;
	cout << wboard.size() << endl;
	for(int i = 0; i < rec.size(); ++ i){
		cv::rectangle(wboard, 
			Point(rec[i].x, rec[i].y),
			Point(rec[i].x + rec[i].w, rec[i].y + rec[i].h),
			Scalar(255, 0, 0),
			3, 4, 0
		);
	}
	namedWindow("mywindow");
	imshow("mywindow", wboard);
	waitKey(0);
	return ;
}
int main(int argc, char* argv[])
{
	FILE* data_file = fopen("./test_data.txt", "r");
	vector<Bbox> bx;
	int n; // the mount will process
	fscanf(data_file, "%d", &n);
	for(int i = 0; i < n; ++ i){
		Bbox bbx;
		//cin >> bbx.x >> bbx.y >> bbx.w >> bbx.h >> bbx.score;
		fscanf(data_file, "%lf %lf %lf %lf %lf", &bbx.x, &bbx.y, &bbx.w, &bbx.h, &bbx.score);
		bx.push_back(bbx);
	}
	cout << "end input" << endl;
	box_show(bx);
	NMS nms(bx, 0.6);
	vector<Bbox> res = nms.nms();
	box_show(res);
	cout << "num :" << res.size() << endl;
	for(int i = 0; i < res.size(); ++i){
		cout << res[i].x << " " << res[i].y << " " << res[i].w << " " << res[i].h << " " << res[i].score << endl;
	}
	return 0;
}