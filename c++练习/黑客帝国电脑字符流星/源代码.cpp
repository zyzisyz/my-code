#include <windows.h>
#include <time.h>
#include <stdlib.h>
#include <graphics.h>										//���û��graphics�⣬���Ե�  http://www.easyx.cn/ ����
#include <conio.h>
#include <math.h>


#define PI 3.1415926										//Բ����
#define WIDTH 1920											//��Ļ��ȣ����ǳ�������
#define HEIGHT 1080											//��Ļ�߶ȣ����ǳ�������
#define V 20												//�����ٶȣ������ƶ���������
#define LENGTH	30											//�����ַ���
#define DELAY 20											//��ʱ
#define NUM 30												//���Ǹ���
#define SIZE

struct meteor												//meteor�����ǵ���˼
{
	int x0;
	int y0;
	int yh;
	char str[LENGTH];
}me[NUM] = { 0 };

char AsciiRand() { return ((char)(rand() % (93) + 33)); }

void Move(char *p)
{
	char *pt = p + LENGTH;
	while (pt > p)
	{
		*(--pt) = *(pt - 1);
	}
	*p = AsciiRand();
}

void InitMeteor(meteor *me)
{
	me->x0 = rand() % WIDTH;
	me->yh = me->y0 = rand() % HEIGHT;
	for (int i = 0; i < LENGTH; i++)
		*(me->str + i) = AsciiRand();
}

int color(int y, int y0, int yh)
{
	int color;
	if (y < y0)
		color = 0;
	else
		color = (int)(255 * cos((yh - y) * PI / (2 * LENGTH * V)));
	return color;
}

void Meteors(struct meteor me[])
{
	setbkmode(TRANSPARENT);
	settextstyle(15,15,"����");
	int y;
	for (int n = 0; n < NUM; n++)
	{
		for (int j = 0; j < LENGTH; j++)
		{
			y = me[n].yh - j * V;
			setcolor(RGB(255 * (0 == j), color(y, me[n].y0, me[n].yh), 255 * (0 == j)));
			outtextxy(me[n].x0, y, me[n].str[j]);
		}
	}
}
int main(void)
{
	char c = '\0';
	initgraph(WIDTH, HEIGHT);
	HWND hwnd = GetHWnd();
	ShowWindow(hwnd, SW_SHOWMAXIMIZED);
	srand((unsigned)time(NULL));
	for (int i = 0; i < NUM; i++)
		InitMeteor(&me[i]);
	while (c != 27)                         //char c �ó���һֱ����
	{
		BeginBatchDraw();
		Meteors(me);
		FlushBatchDraw();
		Sleep(DELAY);
		cleardevice();
		for (int i = 0; i < NUM; i++)
		{
			me[i].yh += V;
			Move(me[i].str);
			if (me[i].yh > HEIGHT + LENGTH * V)
				InitMeteor(&me[i]);
		}
	}
	EndBatchDraw();
	closegraph();
}