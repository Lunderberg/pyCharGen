

#include "LendaEvent.hh"
#include <iostream>
#include "TMath.h"
#include <sstream>

using namespace std;


#define BAD_NUM -1008
LendaEvent::LendaEvent()
{
  fPosForm="chan";
  sdt1=0;
  sdt2=0;
  fgainCorrections.clear();
  fwalkCorrections.clear();
  fnumOfWalkCorrections=0;
  fnumOfGainCorrections=0;
  fnumOfPositionCorrections=0;
  

  Clear();


}
LendaEvent::LendaEvent(bool BuildMap){
  LendaEvent();
  if (BuildMap)
    DefineMap();
  
}


void LendaEvent::setWalkCorrections(vector <Double_t> in){
  fwalkCorrections.clear();
  fwalkCorrections.push_back(in);
  fnumOfWalkCorrections=0;
}

void LendaEvent::setWalkCorrections(vector <Double_t> in,Int_t channel){

  if (channel >= (Int_t)fwalkCorrections.size() ){
    int diff = channel-fwalkCorrections.size();
    fwalkCorrections.resize( fwalkCorrections.size()+diff +1);
  }
  
  fwalkCorrections[channel]=in;


  fnumOfWalkCorrections++;
}

void LendaEvent::setGainCorrections(vector <pair <Double_t,Double_t> > in ){
  for (int i=0;i<(int)in.size();i++)
    setGainCorrections(in[i].first,in[i].second,i);
}

void LendaEvent::setGainCorrections(Double_t slope,Double_t c,Int_t channel){

  if (channel >= (Int_t)fgainCorrections.size()){
    int diff = channel - fgainCorrections.size();
    fgainCorrections.resize(fgainCorrections.size()+diff+1,make_pair(1.0,0));
  }
  fgainCorrections[channel]=make_pair(slope,c);


  fnumOfGainCorrections++;
}
void LendaEvent::PrintList(){
  /*  DumpCorrectionsMap();
  cout<<"The mapping between Corrections and names is"<<endl;
  CorMap=mapForCorrectionResults;
  for (map<string,int>::iterator ii =CorMap.begin();ii!=CorMap.end();ii++)
    cout<<ii->first<<"  "<<ii->second<<endl;
  */
  AddMapEntry("energies",&energies);
}

void LendaEvent::Clear(){
  ////REMEBER TO CLEAR THINGS THAT were thing.push_Back!!!!
  TOF=BAD_NUM;
  Dt=BAD_NUM;
  
  NumBadPoints=0;

  ShiftDt=BAD_NUM;
  ShiftTOF=BAD_NUM;

  GOE=BAD_NUM;
  CorGOE=BAD_NUM;
  PulseShape=BAD_NUM;

  TOFW.clear();
  TOFP.clear();

  times.clear();
  energies.clear();
  energiesCor.clear();
  internEnergies.clear();
  channels.clear();
  softwareCFDs.clear();
  internalCFDs.clear();
  softTimes.clear();
  cubicTimes.clear();

  Traces.clear();
  Filters.clear();
  CFDs.clear();

  entryNums.clear();

  shortGates.clear();
  longGates.clear();


  shiftCorrectedTimes.clear();

  // heDynamicCorrectionResults.clear();


  NumOfChannelsInEvent=0;

}

void LendaEvent::pushTime(Double_t t){
  times.push_back(t);

}
void LendaEvent::pushEnergy(Double_t e){
  energies.push_back(e);

}
void LendaEvent::pushChannel(Double_t c){
  channels.push_back(c);
}

void LendaEvent::pushTrace(vector <UShort_t> in){
  Traces.push_back(in);
}
void LendaEvent::pushFilter(vector <Double_t> in){
  Filters.push_back(in);
}
void LendaEvent::pushCFD(vector <Double_t> in){
  CFDs.push_back(in);
}

void LendaEvent::pushInternalCFD(Double_t t){
  internalCFDs.push_back(t);
}
void LendaEvent::pushSoftwareCFD(Double_t t){
  softwareCFDs.push_back(t);
}
void LendaEvent::pushSoftTime(Double_t t){
  softTimes.push_back(t);
}

void LendaEvent::pushEntryNum(Long64_t t){
  entryNums.push_back(t);
}
void LendaEvent::pushCubicTime(Double_t t){
  cubicTimes.push_back(t);
}


void LendaEvent::pushLongGate(Double_t lg){
  longGates.push_back(lg);
}
void LendaEvent::pushShortGate(Double_t sg){
  shortGates.push_back(sg);
}
void LendaEvent::pushInternEnergy(Double_t t){
  internEnergies.push_back(t);
}

void LendaEvent::shiftCor(){

  // correction to move the time difference spectrum seen in a lenda bar
  // to be around 0
  //correction determined from time[0]-time[1]
  //shift applied to time[0]
  if (channels[0]==0 && channels[1] ==1 ) {//one bar
    shiftCorrectedTimes.push_back(times[0]-sdt1);


  } else if (channels[0]==2 && channels[1]==3) { //the other one
    shiftCorrectedTimes.push_back(times[0]-sdt2);


  }

  shiftCorrectedTimes.push_back(times[1]); //time[1] is unchanged
  shiftCorrectedTimes.push_back(times[2]);//time[2] is unchanged

}

void LendaEvent::gainCor(){

  //Applying gain correction to each of the channels for Lenda bars
  
  for (int i=0;i<(int)energies.size();i++){
    energiesCor[i]=energies[i]*fgainCorrections[channels[i]].first +
      fgainCorrections[channels[i]].second;

  }
}

void LendaEvent::walkCor(){
  Double_t total[fnumOfWalkCorrections];

  for (int i=0;i<fnumOfWalkCorrections;i++)
    total[i]=0;

  
  for (int j=0;j<fnumOfWalkCorrections;j++){
    if (channels[j]<fwalkCorrections.size()){
      for (int i=0;i<(int)fwalkCorrections[channels[j]].size();i++){
	
	//	if (energiesCor[j]<600)
	  total[j]=total[j]+fwalkCorrections[channels[j]][i]*TMath::Power(energiesCor[j],i+1);

      }
    }
  }


  Double_t runningTotal=0;
  for (int j=0;j<fnumOfWalkCorrections;j++){
     runningTotal = runningTotal +total[j];
     //     cout<<"This is runningTotal "<<runningTotal<<" this is J "<<j<<endl;
     // int t ;cin>>t;
     TOFW[j]=fTimeAfterPosCor-runningTotal;
  }
    
}


void LendaEvent::Finalize(){

  energiesCor.resize(energies.size());
  TOFW.resize(fnumOfWalkCorrections);
  TOFP.resize(fnumOfPositionCorrections);
  shiftCor();//make the shiftCorrectedTimes
 
  if (fgainCorrections.size()!=0)//only apply gain correctins if 
    gainCor();                   //they have be provided

  /*
  if (Traces.size()!=0){
    for (int j=0;j<Traces.size();j++){
      double avg =0;
      if (Traces[j].size()>20){
	for (int a=0;a<20;a++)
	  avg = Traces[j][a] +avg;
	avg=avg/20.0;
	for (int i=0;i<Traces[j].size();i++){
	  if (Traces[j][i]< 0.9*avg)
	    NumBadPoints++;
	}
      }
    }
  }
  */

  E0=energiesCor[0];
  E1=energiesCor[1];
  E2=energiesCor[2];
  E3=energiesCor[3];


  TOF = 0.5*(times[0]+times[1])-times[2];
  ShiftDt=(shiftCorrectedTimes[0]-shiftCorrectedTimes[1]);
  ShiftTOF=0.5*(shiftCorrectedTimes[0]+shiftCorrectedTimes[1]) -shiftCorrectedTimes[2];


  NumOfChannelsInEvent = times.size();//the number of channels pushed to event
  PulseShape = longGates[2]/shortGates[2];

  Dt = times[0]-times[1];
  
  CDt= cubicTimes[0]-cubicTimes[1];

  GOE = (energies[0]-energies[1])/(energies[0]+energies[1]);
  CorGOE = (energiesCor[0]-energiesCor[1])/(energiesCor[0]+energiesCor[1]);
  //  posCor();  

  //  if (fwalkCorrections.size()!=0)
  //  walkCor();
  
  ApplyDynamicCorrections();

}

void LendaEvent::setPositionCorrections(vector <Double_t> coef,Int_t channel ){

  stringstream key;
  key<<fPosForm<<"_"<<channel;

  if (fPositionCorrections.find(key.str()) == fPositionCorrections.end()){
    fPositionCorrections[key.str()]=coef;
    fnumOfPositionCorrections++;
  }else {
    cout<<"***Warning correction with key "<<key.str()<<" has already exists***"<<endl;
    cout<<"***Choose different key***"<<endl;
  }
}

void LendaEvent::posCor(){
  //Apply the position correctioins

  

  Double_t total[fnumOfPositionCorrections];

  for (int i=0;i<fnumOfPositionCorrections;i++)
    total[i]=0;

  stringstream key;
  vector <Double_t> theCoef;
  for (int j=0;j<fnumOfPositionCorrections;j++){
    key.str("");
    key<<fPosForm<<"_"<<channels[j];
    if (fPositionCorrections.find(key.str()) != fPositionCorrections.end()){
      theCoef =fPositionCorrections[key.str()];
      for (int i=0;i<theCoef.size();++i){
	total[j]=total[j]+ theCoef[i]*TMath::Power(CorGOE,i+1);


      }
    }
  }

  Double_t runningTotal=0;
  for (int j=0;j<fnumOfPositionCorrections;j++){
    runningTotal=runningTotal+total[j];
    TOFP[j]=ShiftTOF-runningTotal;    

  }


  if (TOFP.size()!=0)
    fTimeAfterPosCor=TOFP[TOFP.size()-1];
  else
    fTimeAfterPosCor=ShiftTOF;

  /*
    if (channels[j]<fwalkCorrections.size()){
      for (int i=0;i<(int)fwalkCorrections[channels[j]].size();i++){

        //      if (energiesCor[j]<600)
	total[j]=total[j]+fwalkCorrections[channels[j]][i]*TMath::Power(energiesCor[j],i+1);

      }
    }
  }

  Double_t runningTotal=0;
  for (int j=0;j<fnumOfWalkCorrections;j++){
    runningTotal = runningTotal +total[j];
    //     cout<<"This is runningTotal "<<runningTotal<<" this is J "<<j<<endl;
    // int t ;cin>>t;
    TOFW[j]=ShiftTOF-runningTotal;
  }


  */


}


void LendaEvent::DumpWalkCorrections(){
  cout<<"\n***Dump walk corrections***"<<endl;

  for (int j=0;j<(int)fwalkCorrections.size();++j){
    int max_i = fwalkCorrections[j].size();
    cout<<"walkCorrection for channel "<<j<<endl;
    for (int i=0;i<max_i;++i){
      cout<<"   c"<<i+1<<" "<<fwalkCorrections[j][i]<<endl;
      //i+1 because the coefficents don't include the constant term
    }
  }
  

}

void LendaEvent::DumpGainCorrections(){
  cout<<"\n***Dump gain Corrections***"<<endl;
  for (int i=0;i<(int)fgainCorrections.size();++i){
    cout<<"gain correction for channel "<<i<<" "<<fgainCorrections[i].first<<" "
	<<fgainCorrections[i].second<<endl;
  }
}

void LendaEvent::DumpAllCorrections(){
  DumpGainCorrections();
  DumpWalkCorrections();
  DumpPositionCorrections();
}


void LendaEvent:: DumpPositionCorrections(){
  
for( map<string,vector<double> >::iterator ii=fPositionCorrections.begin(); ii!=fPositionCorrections.end(); ++ii)
    {
      for (int i=0;i<(int)((*ii).second).size();++i)
	cout << (*ii).first<<" "<<i << ": " << (*ii).second[i] << endl;
    }


}

void LendaEvent::Fatal(){
  cout<<"This Method should not exist.  Don't call it"<<endl;
}


void LendaEvent::MakeC(int spot){
  /*  
  cout<<"this is CTrace "<<CTrace<<endl;
  
  if (CTrace != 0){
    cout<<"Free CTrace"<<endl;
    free(CTrace);
    CTrace=0;
    
  }
  if (CFilter !=0){
    cout<<"Free CFilter"<<endl;
    free(CFilter);
    CFilter=0;
  }

  if (CCFD !=0 ){
    cout<<"Free CCFD"<<endl;
    free(CCFD);
    CCFD=0;
  }

  if (Traces.size()!=0 &&Traces[spot].size() != 0 ){
    cout<<"Allocate CTrace"<<endl;
    CTrace = (UShort_t*)calloc(sizeof(UShort_t),Traces[spot].size());
  }
  
  if (Filters.size() !=0 && Filters[spot].size() != 0){
    cout<<"Allocate CFilter"<<endl;
    CFilter = (Double_t*)calloc(sizeof(Double_t),Traces[spot].size());
  }
  
  if (CFDs.size() !=0 && CFDs[spot].size() != 0 ){
    cout<<"Allocate CCFD"<<endl;
    CCFD = (Double_t*)calloc(sizeof(Double_t),Traces[spot].size());
  }
  
  for (int i=0;i<Traces[spot].size();i++){
    if (CTrace != 0)
      CTrace[i]=Traces[spot][i];
    if (CFilter !=0 )
      CFilter[i]=Filters[spot][i];
    if ( CCFD !=0 )
      CCFD[i]=CFDs[spot][i];
  }
  */
}



LendaEvent & LendaEvent::operator = (const LendaEvent&  right){

  this->Clear();

  this->energiesCor = right.energiesCor;
  this->times = right.times;
  this->softTimes = right.softTimes;
  this->cubicTimes = right.cubicTimes;
  this->energies = right.energies;
  this->internEnergies=right.energies;
  this->channels = right.channels;
  this->softwareCFDs =right.softwareCFDs;
  this->internalCFDs =right.internalCFDs;
  this->entryNums=right.entryNums;
  this->Traces = right.Traces;
  this->Filters = right.Filters;
  this->CFDs = right.CFDs;
  this->longGates =right.longGates;
  this->shortGates =right.shortGates;

  
  return *this;

}


///////BEGIN __AUTO__ GENERATED///////
void LendaEvent::DefineMap(){
theVariableMap["TOF"]=&TOF;
theVariableMap["Dt"]=&Dt;
theVariableMap["ShiftTOF"]=&ShiftTOF;
theVariableMap["ShiftDt"]=&ShiftDt;
theVariableMap["E0"]=&E0;
theVariableMap["E1"]=&E1;
theVariableMap["E2"]=&E2;
theVariableMap["E3"]=&E3;
theVariableMap["CDt"]=&CDt;
theVariableMap["NumBadPoints"]=&NumBadPoints;
theVariableMap["PulseShape"]=&PulseShape;
theVariableMap["GOE"]=&GOE;
theVariableMap["CorGOE"]=&CorGOE;
theVariableMap["energies"]=&energies;
theVectorVariableMap["energies"]=&energies;
theVariableMap["energiesCor"]=&energiesCor;
theVectorVariableMap["energiesCor"]=&energiesCor;
}
 
