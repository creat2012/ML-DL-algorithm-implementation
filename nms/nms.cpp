#include "nms.hpp"
#include <algorithm>
// for sort
bool cmp(Bbox x1, Bbox x2)
{
	if(x1.score > x2.score) return true;
	else return false;
}

NMS::NMS(vector<Bbox> bbox_, double shreshold_)
{
	this->bbox = bbox_;
	this->shreshold = shreshold_;
}

double NMS::IOU(Bbox b1, Bbox b2)
{
	double iou;
	double minx, miny, maxx, maxy;
	minx = max(b1.x, b2.x);
	miny = max(b1.y, b2.y);
	maxx = min(b1.x + b1.w, b2.x + b2.w);
	maxy = min(b1.y + b1.h, b2.y + b2.h);
	double overlap_w = max(0.0, maxx - 	minx);
	double overlap_h = max(0.0, maxy - miny);
	double overlap = overlap_h * overlap_w; 
	iou = overlap / (b1.w * b1.h + b2.w * b2.h - overlap);
	return iou;
}
void NMS::print_box_info(std::vector<Bbox> boxes)
{
	cout << "begin output boxes information" << endl;
	for(int i = 0; i < boxes.size(); ++ i){
		cout << "the " << i << "th box : " << boxes[i].x << boxes[i].y << boxes[i].w << boxes[i].h << boxes[i].score << endl;
	}
	cout << "end ouput boxes information" << endl;
}
vector<Bbox> NMS::nms()
{
	int pos = 0;
	// sort by the score
	sort(bbox.begin(), bbox.end(), cmp);
	print_box_info(bbox);
	while(bbox.size()){
		res.push_back(bbox[0]);
		for(int i = 1; i < bbox.size(); ++ i){
			cout << IOU(bbox[0], bbox[i]) << endl;
			if(IOU(bbox[0], bbox[i]) > this->shreshold){
				bbox.erase(bbox.begin() + i);
				-- i;
			}
		}
		bbox.erase(bbox.begin());
		print_box_info(bbox);
	}
	return res;
}
NMS::~NMS()	
{
	//delete[] bbox;
}