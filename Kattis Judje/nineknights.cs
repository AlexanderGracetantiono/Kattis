using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace knight
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string[,] board = new string[5,5];
            string cek = "valid";
            int sumK = 0;

            for(int y = 0; y < 5; y++)
            {
                string text = Console.ReadLine();
                for (int x= 0; x < 5; x++)
                {
                    if (text[x] == 'k') { sumK++; }
                    board[y, x] = text[x] + "";
                   
                }
            }
            for (int y = 0; y < 5; y++)
            {
                for (int x = 0; x < 5; x++)
                {
                    if (board[y, x] == "k")
                    {//11==32 23,, 13==12 23 43 52,, 33 ==12 14 21 25 41 45 52 54
                     //3-2,3-1  3-1,3-2      
                     //3+2,3+1  3+1,3+2
                     //3-2,3+1  3-1,3+2
                     //3+2,3-1  3+1,3-2 
                        if (y - 2 > 0&&x-1>0)
                        {
                            if (board[y - 2, x - 1] == "k") { cek = "invalid"; }
                        }
                        if (y - 2 > 0 && x + 1 < 5)
                        {
                            if (board[y - 2, x + 1] == "k") { cek = "invalid"; }
                        }
                        if (y + 2 < 5 && x - 1 > 0)
                        {
                            if (board[y + 2, x - 1] == "k") { cek = "invalid"; }
                        }
                        if (y + 2 < 5 && x + 1 <5)
                        {
                            if (board[y + 2, x + 1] == "k") { cek = "invalid"; }
                        }
                        //////////////////////////////////////////////////////////////
                        if (x - 2 > 0 && y - 1 > 0)
                        {
                            if (board[y - 1, x - 2] == "k") { cek = "invalid"; }
                        }
                        if (x - 2 > 0 && y + 1 < 5)
                        {
                            if (board[y +1, x - 2] == "k") { cek = "invalid"; }
                        }
                        if (x + 2 < 5 && y - 1 > 0)
                        {
                            if (board[y -1, x + 2] == "k") { cek = "invalid"; }
                        }
                        if (x + 2 < 5 && y + 1 < 5)
                        {
                            if (board[y + 1, x + 2] == "k") { cek = "invalid"; }
                        }

                    }

                }
            }
            if (sumK != 9) { cek = "invalid"; }
            Console.WriteLine(cek);
            Console.ReadKey();

    

        }
    }
}