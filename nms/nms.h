struct Bbox
{
	int x, y, w, h; // bounding box's up-left point, and width , height
	double score;
};

class NMS
{
public:
	NMS(Bbox *bbox, int);
	~NMS();
private:
	Bbox *bbox;
	Bbox *res;
	int n;
};