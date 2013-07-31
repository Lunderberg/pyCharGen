#ifndef __LENDA_EVENT_HH
#define __LENDA_EVENT_HH

#include "TObject.h"
#include "TFile.h"
#include "Correctable.hh"
#include <vector>
#include <map>

using namespace std;

class LendaEvent :  public Correctable  {
public:

  LendaEvent(); //Constructor 
  LendaEvent(bool BuildMap);
  void Clear(); //Clear the Event.  Should be called after every write to a tree

  void Finalize(); //Applies internal corrections and calculates convient Branches/leaves

  virtual void DefineMap(); //Inherited from Correctable defines var look up
  void PrintList();
 
  //Convenient quantities calculated in Finalize
  Double_t TOF; // Time of flight //__var
  Double_t Dt; //Diference between Top and botom PMTs //__var
  Double_t ShiftTOF; //TOF after shift correction //__var
  Double_t ShiftDt;  //Dt after shift correction//__var

  Double_t E0;//__var
  Double_t E1;//__var
  Double_t E2;//__var
  Double_t E3;//__var

  Double_t CDt;//__var

  Int_t NumBadPoints;//__var

  Double_t PulseShape; //long gate over short gate  //__var
  Double_t GOE;   //Center of Gravity (E1-E2)/(E1+E2)  //__var
  Double_t CorGOE;//Center of Gravity after gain matching //__var
  vector <Double_t> TOFW; // the Walk corrections to TOF 
  vector <Double_t> TOFP; //The position Corrections to TOF

  //  vector<Double_t> Corrections;
  map <string,int> CorMap;
  //Main information holders
  vector <Double_t> energiesCor; //the corrected energies 
  vector <Double_t> times; //the times
  vector <Double_t> softTimes;
  vector <Double_t> cubicTimes;
  vector <Double_t> energies; // the raw energies
  vector <Double_t> internEnergies;
  vector <Double_t> channels; // the channels
  vector <Double_t> softwareCFDs;
  vector <Double_t> internalCFDs;
  vector <Long64_t> entryNums;

  vector < vector <UShort_t> > Traces; // a vector of vectors holding the traces if present
  vector < vector <Double_t> > Filters; //a vector of vectors for the filters if present
  vector < vector <Double_t> > CFDs;  // a vector of vectors for the CFDs if present
  
  

  vector <Double_t> shiftCorrectedTimes; //The shift corrected times
  vector <Double_t> shortGates;  //short gate energies
  vector <Double_t> longGates;  //long gate energies



  //C Trace thing
  //root like c arrays more then vectors of vectors
  void MakeC(int spot=0);  //copy trace,FF,CFD data for the spot-th trace into C-arrays
  //the c-array to store the trace in



  //pushing methods expects the series of times and energies to be ordered by channel
  void pushLongGate(Double_t);
  void pushShortGate(Double_t);
  void pushEnergy(Double_t);
  void pushInternEnergy(Double_t);
  void pushTime(Double_t);
  void pushChannel(Double_t);
  void pushTrace (vector <UShort_t>);
  void pushFilter (vector <Double_t>);
  void pushCFD (vector <Double_t>);
  void pushInternalCFD(Double_t);
  void pushSoftwareCFD(Double_t);
  void pushSoftTime(Double_t);
  void pushEntryNum(Long64_t);
  void pushCubicTime(Double_t);

  Int_t NumOfChannelsInEvent; //The Number of channels associated with this event

  //Corrections setting methods
  inline void setShiftCorrections(Double_t c1,Double_t c2){sdt1=c1;sdt2=c2;}//set shift Cor
  void setGainCorrections(Double_t slope,Double_t c,Int_t channel);//sets the gain correction for a channel
  void setGainCorrections(vector <pair <Double_t,Double_t> > );//wrapper to the above assumes the vector has channel 0 at 
                                              //index 0 and channel 1 at index 1 ...


  void setWalkCorrections(vector <Double_t> in); //This sets input walkcorrection as the first 
                                                 //correction in the set walkCorrections[0][i] i goes 
                                                 //from 1 to degree of correction

  void setWalkCorrections(vector <Double_t> in,Int_t channel); // sets the correction and puts it in the 
                                                               //walkCorrections[channel][i]


  void setPositionCorrections(vector <Double_t>,Int_t channel );//sets the position correction a channel




  void DumpWalkCorrections();
  void DumpGainCorrections();
  void DumpAllCorrections();
  void DumpPositionCorrections(); 


  
  LendaEvent& operator = (const LendaEvent &right);



  void Fatal();//overload this stupid inherited method

private:
  void shiftCor(); //method to apply the shift corections
  void gainCor(); //method to apply the gain corrections
  void walkCor(); //method to apply the walk corrections
  void posCor(); //method to apply the position corrections

  //Corecction 
  Double_t sdt1,sdt2;

  vector < pair<Double_t,Double_t> > fgainCorrections; //the gain corrections 
  vector < vector <Double_t> > fwalkCorrections; // set of walkCorrections

  map <string,vector<Double_t> > fPositionCorrections;//map for the position corrections 

  int fnumOfWalkCorrections; // number of walk corrections
  int fnumOfGainCorrections;// number of Gain corrections
  int fnumOfPositionCorrections;// number of position corrections

  string fPosForm; 
  
  double fTimeAfterPosCor; //the time after the pos cor which the walk cor is applied to
  
public:
  ClassDef(LendaEvent, 12);
};

#endif



