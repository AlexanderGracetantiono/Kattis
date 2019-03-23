using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2048
{
    class Program
    {
        static void Main(string[] args)
        {//0=left, 1=up 2,right,3=down
            string[,] game = new string[4, 4];
            string[,] fix = new string[4, 4];
            for (int y = 0; y < 4; y++)
            {
                string[] text = Console.ReadLine().Split(' ');
                for (int x = 0; x < 4; x++)
                {
                    fix[y, x] = "false";
                    game[y, x] = text[x];
                }
            }

            int move = int.Parse(Console.ReadLine());

            if (move == 0)
            {
                for (int y = 0; y < 4; y++)
                {
                    int x = 0;
                    int count = 3;
                    do
                    {
                        if (x <3)
                        {
                           
                               // Console.WriteLine("test : " + game[y, x + 1] + " " + game[y, x]);

                                if (game[y, x] == "0")
                                {
                                    game[y, x] = game[y, x+1];
                                    game[y, x+1] = "0";
                                if(fix[y,x+1] == "true")
                                {
                                    fix[y, x] = "true";
                                    fix[y, x+1] = "false";
                                }
                              

                                }
                                else if (game[y, x+1] == game[y, x])
                                {
                                if (fix[y, x] == "false" && fix[y, x+1] == "false")
                                {
                                    game[y, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x + 1] = "0";
                                    fix[y, x] = "true";
                                }
                                   

                                }
                           x++;
                        }
                        else
                        {
                            x = 0;
                            count--;
                    
                        }

                    } while (count != 0);
                }
            }
            //////////////////////////////////////////////////////////////////////////////////////////////////

            if (move == 2)
            {
                for (int y = 0; y < 4; y++)
                {
                    int x = 3;
                int count = 3;
                    do
                    {
                        if (x >0)
                        {          
                           // Console.WriteLine("test : " + game[y, x - 1] + " " + game[y, x]);

                            if (game[y, x] == "0")
                            {
                                game[y, x] = game[y, x - 1];
                                game[y, x - 1] = "0";
                                if (fix[y, x - 1] == "true")
                                {
                                    fix[y, x] = "true";
                                    fix[y, x - 1] = "false";
                                }


                            }
                            else if (game[y, x - 1] == game[y, x])
                            {
                                if (fix[y, x] == "false" && fix[y, x-1] == "false")
                                {
                                    game[y, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x - 1] = "0";
                                    fix[y, x] = "true";
                                }


                            }
                            x--;
                        }
                        else
                        {
                            x = 3;
                        count--;
                        }

                    } while (count != 0);
                }
            }
            /////////////////////////////////////////////////////////////////////////////////////////////////////////
            if (move == 3)
            {
                for (int x = 0; x < 4; x++)
                {
                    int y = 3;
                    int count = 3;
                    do
                    {
                        if (y > 0)
                        {
                           // Console.WriteLine("test : " + game[y-1, x] + " " + game[y, x]);

                            if (game[y, x] == "0")
                            {
                                game[y, x] = game[y-1, x];
                                game[y-1, x] = "0";
                                if (fix[y-1, x] == "true")
                                {
                                    fix[y, x] = "true";
                                    fix[y-1,x] = "false";
                                }


                            }
                            else if (game[y-1, x] == game[y, x])
                            {
                                if (fix[y, x] == "false" && fix[y-1, x] == "false")
                                {
                                    game[y, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y-1, x] = "0";
                                    fix[y, x] = "true";
                                }


                            }
                            y--;
                        }
                        else
                        {
                            y = 3;
                            count--;
                        }

                    } while (count != 0);
                }
            }
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////
            if (move == 1)
            {
                for (int x = 0; x < 4; x++)
                {
                    int y = 0;
                    int count = 3;
                    do
                    {
                        if (y < 3)
                        {
                           /// Console.WriteLine("test : " + game[y + 1, x] + " " + game[y, x]);

                            if (game[y, x] == "0")
                            {
                                game[y, x] = game[y + 1, x];
                                game[y + 1, x] = "0";
                                if (fix[y + 1, x] == "true")
                                {
                                    fix[y, x] = "true";
                                    fix[y + 1, x] = "false";
                                }


                            }
                            else if (game[y + 1, x] == game[y, x])
                            {
                                if (fix[y, x] == "false" && fix[y + 1, x] == "false")
                                {
                                    game[y, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y + 1, x] = "0";
                                    fix[y, x] = "true";
                                }


                            }
                            y++;
                        }
                        else
                        {
                            y = 0;
                            count--;
                        }

                    } while (count != 0);
                }
            }

            /*
           else if (move == 0)
            {
                for (int y = 0; y < 4; y++)
                {
                    //klo x-1==0, x--;
                    int batas = 0;
                    int x = 3;
                    int count = 3;
                    do
                    {
                        if (x > batas)
                        {
                           if (game[y, x] != "0")
                           {
                               // Console.WriteLine("test : " + game[y, x - 1] + " " + game[y, x]);
                         
                                if (game[y, x - 1] == "0")
                                {
                                    game[y, x - 1] = game[y, x];
                                    game[y, x] = "0";
                                   
                                }
                                else if (game[y, x - 1] == game[y, x])
                                {
                                    game[y, x - 1] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x] = "0";
                                   
                                }
                               
                            }
                            x--;
                        }
                        else
                        {
                            x = 3;
                            count--;
                            batas++;
                        }

                    } while (count != 0);
                }
            }

            else if (move == 2)
            {
                for (int y = 0; y < 4; y++)
                {
                    //klo x-1==0, x--;
                    int batas = 3;
                    int x = 0;
                    int count = 3;
                    do
                    {
                        if (x < batas)
                        {
                            if (game[y, x] != "0")
                            {
                                if (game[y, x + 1] == "0")
                                {
                                    game[y, x + 1] = game[y, x];
                                    game[y, x] = "0";
                                }
                                else if (game[y, x + 1] == game[y, x])
                                {
                                    game[y, x + 1] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x] = "0";
                                }
                            }
                            x++;
                        }
                        else
                        {
                            x = 0;
                            batas--;
                            count--;
                        }

                    } while (count != 0);
                }
            }

          else  if (move == 1)
            {
                for (int x = 0; x < 4; x++)
                {
                    int batas = 0;
                    int y = 3;
                    int count = 3;
                    do
                    {
                        if (y > batas)
                        {
                            if (game[y, x] != "0")
                            {
                                if (game[y - 1, x] == "0")
                                {
                                    game[y - 1, x] = game[y, x];
                                    game[y, x] = "0";
                     
                                }
                                else if (game[y - 1, x] == game[y, x])
                                {
                                    game[y - 1, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x] = "0";
                                 
                                }
                            }
                            y--;
                        }
                        else
                        {
                            y = 3;
                            count--;
                            batas++;
                        }

                    } while (count != 0);
                }
            }


            else if (move == 3)
            {
                for (int x = 0; x < 4; x++)
                {
                    int batas = 3;
                    int y = 0;
                    int count = 3;
                    do
                    {
                        if (y > batas)
                        {
                            if (game[y, x] != "0")
                            {
                                if (game[y + 1, x] == "0")
                                {
                                    game[y + 1, x] = game[y, x];
                                    game[y, x] = "0";
                             
                                }
                                else if (game[y + 1, x] == game[y, x])
                                {
                                    game[y + 1, x] = (int.Parse(game[y, x]) * 2) + "";
                                    game[y, x] = "0";
                                 
                                }
                            }
                            y++;
                        }
                        else
                        {
                            y = 0;
                            count--;
                            batas--;
                        }

                    } while (count != 0);
                }
            }
            */
            for (int y = 0; y < 4; y++)
            {
                for(int x = 0; x < 4; x++)
                {
                    Console.Write(game[y, x] + " ");
                }
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
