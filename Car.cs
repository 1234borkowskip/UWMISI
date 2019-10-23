using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Car
    {
        public string marka;
        public string rok;
        private string model;
        private int iloscDrzwi;
        private double pojemnoscSilnika;
        public double srednieSpalanie;

        private double ObliczSpalanie(double dlugoscTrasy)
        {
            double spalanie = srednieSpalanie * dlugoscTrasy;
            return spalanie;
        }

        public ObliczKosztPrzejazdu( double dlugoscTrasy, double cenaPaliwa)
        {
            double kosztPrzejazdu = ObliczSpalanie(dlugoscTrasy) * cenaPaliwa;
            return kosztPrzejazdu;
        }
    }
}
