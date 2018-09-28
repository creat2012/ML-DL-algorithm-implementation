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
	minx = min(b1.x, b2.x);
	miny = min(b1.y, b2.y);
	maxx = max(b1.x + b1.w, b2.x + b2.w);
	maxy = max(b1.y + b1.h, b2.y + b2.h);
	double overlap_w = max(0.0, maxx - 	minx);
	double overlap_h = max(0.0, maxy - miny);
	double overlap = overlap_h * overlap_w; 
	iou = overlap / (b1.w * b1.h + b2.w * b2.h - overlap);
	return iou;
}

vector<Bbox> NMS::nms()
{
	int pos = 0;
	// sort by the score
	sort(bbox.begin(), bbox.end(), cmp);
	while(bbox.size()){
		res.push_back(bbox[0]);
		for(int i = 1; i < bbox.size(); ++ i){
			cout << IOU(bbox[0], bbox[i]) << endl;
			if(IOU(bbox[0], bbox[i]) > 0.8){
				bbox.erase(bbox.begin() + i);
				-- i;
			}
		}
		bbox.erase(bbox.begin());
	}
	return res;
}
NMS::~NMS()	
{
	//delete[] bbox;
}