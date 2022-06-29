#pragma once

struct Data{
	long timestamp;
	double x, y, z;
	int type; // 0 wheel; 1 acc ; 2 gyr
};

class TimeProcessor
{
public:
	TimeProcessor();
	~TimeProcessor();
};

