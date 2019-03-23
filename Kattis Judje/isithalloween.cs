using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace istHaloween
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            if(text=="OCT 31"||text== "DEC 25")
            {
                Console.WriteLine("yup");
            }
            else
            {
                Console.WriteLine("nope");
            }
            Console.ReadKey();
        }
    }
}
