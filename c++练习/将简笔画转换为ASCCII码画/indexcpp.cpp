#include <cstdio>
#include <cstdlib>
#include <graphics.h>
#include<iostream>
#include<fstream>
#include<string>
#define ASCII_NUM 32
using namespace std;

struct ascii{
	char asc[ASCII_NUM];
	int gray[ASCII_NUM];
}as = { ' ', '`', '.', '^', ',', ':', '~', '"', '<', '!', 'c', 't', '+', '{', 'i', '7', '?',
'u', '3', '0', 'p', 'w', '4', 'A', '8', 'D', 'X', '%', '#', 'H', 'W', 'M',
0, 5, 7, 9, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
45, 47, 49, 51, 53, 55, 59, 61, 63, 66, 68, 70 };

//二分法查找ASCII字符，向下取值
char SearchAsc(struct ascii as, int gray)
{
	int lower = 0;
	int higher = ASCII_NUM;
	int mid;
	if (gray <= as.gray[0])
		return as.asc[0];
	else if (gray >= as.gray[ASCII_NUM - 1])
		return as.asc[ASCII_NUM - 1];
	else
	{
		while ((higher - lower) > 1)
		{
			mid = (lower + higher) >> 1;
			if (gray > as.gray[mid])
				lower = mid;
			else
				higher = mid;
		}
		return as.asc[lower];
	}
}
void Pic2Asc(ascii as, char filename[], ofstream*a)
{
	int gray;
	IMAGE img;
	loadimage(&img, filename);
	SetWorkingImage(&img);
	int height = 30;
	int width = 60;
	int Part_Width = getheight() / width;
	int Part_Height = getwidth() / height;
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			gray = 0;
			for (int h = 0; h < Part_Height; h++)
				for (int w = 0; w < Part_Width; w++)
				{
					gray += GetRValue(RGBtoGRAY(getpixel(j * Part_Width + w, i * Part_Height + h)));
				}
			gray /= (Part_Height * Part_Width);
			gray = (255 - gray) * 90 / 255;
			cout << SearchAsc(as, gray);
			*a << SearchAsc(as, gray);
		}
		*a << endl;
		cout << endl;
	}
}
int main(void)
{
	cout << "最后一次输出字符将保留在 OuputFile.txt 中" << "\n-----------------------------------------\n" << endl;
	int n;
	char filename[256];
	ofstream OutputFile("OutPutfile.txt");
	while (cout << "请输入图片的路径(含扩展名)" << endl << "可以输入bupt.jpg 或者 test1.jpg 或者 test2.jpg效果演示: " << endl, cin >> filename)
	{
		system("cls");
		ifstream pic(filename);
		if (!pic)
		{
			cout << "没有找到该文件" << endl<<endl;
			continue;
		}
		Pic2Asc(as, filename, &OutputFile);
		OutputFile.close();
	}
}