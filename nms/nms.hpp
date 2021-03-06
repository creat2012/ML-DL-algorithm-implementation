#include <iostream>
#include <vector>
using namespace std;
struct Bbox
{
	double x, y, w, h; // bounding box's up-left point, and width , height
	double score;
};

class NMS
{
public:
	NMS(vector<Bbox> bbox, double);
	~NMS();
	vector<Bbox> nms();
	double IOU(Bbox b1, Bbox b2);
	void print_box_info(std::vector<Bbox>);
private:
	vector<Bbox> bbox;
	vector<Bbox> res;
	double shreshold;
};