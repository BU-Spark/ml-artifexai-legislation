from bs4 import BeautifulSoup
import json

html = """<table id="legislatorTable" class="table table-striped table-centered table-condensed table-borderless table-dark">
                            <thead>
                            <tr>
                                <th scope="col"><span class="sr-only">Follow In My Legislature</span></th>
                                <th scope="col"><span class="sr-only">Legislator Photo</span></th>
                                <th scope="col" class="sortCol " data-managedproperty="FirstName" data-sortdirection="">
    First Name
    <!-- 
        Changed structure to achieve stacking 
        JS will need to be edited for it to work correctly - MD
         -->
    <span class="fa-stack">
        <span class="fa fa-sort fa-stack-1x"></span>
        <span class="fa directionArrow 
             
            fa-stack-1x">
        </span>
    </span>
</th>
                                <th scope="col" class="sortCol " data-managedproperty="LastName" data-sortdirection="asc">
    Last Name
    <!-- 
        Changed structure to achieve stacking 
        JS will need to be edited for it to work correctly - MD
         -->
    <span class="fa-stack">
        <span class="fa fa-sort fa-stack-1x"></span>
        <span class="fa directionArrow 
            fa-sort-up 
            fa-stack-1x">
        </span>
    </span>
</th>
                                <th scope="col">District</th>
                                <th scope="col" class="sortCol " data-managedproperty="PartyTypeId" data-sortdirection="">
    Party
    <!-- 
        Changed structure to achieve stacking 
        JS will need to be edited for it to work correctly - MD
         -->
    <span class="fa-stack">
        <span class="fa fa-sort fa-stack-1x"></span>
        <span class="fa directionArrow 
             
            fa-stack-1x">
        </span>
    </span>
</th>
                                <th scope="col">Room</th>
                                <th scope="col">Phone Number</th>
                                <th scope="col">Email Address</th>
                                
                            </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJB0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJB0.jpg" alt="Michael , Barrett">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJB0">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MJB0">Barrett</a></td>
                                    <td>Third Middlesex</td>
                                    <td>Democrat</td>
                                    <td>312-B</td>
                                    <td>(617) 722-1572</td>
                                    <td>                                            <a href="mailto:Mike.Barrett@masenate.gov">Mike.Barrett@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MDB0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MDB0.jpg" alt="Michael , Brady">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MDB0">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MDB0">Brady</a></td>
                                    <td>Second Plymouth and Norfolk</td>
                                    <td>Democrat</td>
                                    <td>416-A</td>
                                    <td>(617) 722-1200</td>
                                    <td>                                            <a href="mailto:Michael.Brady@masenate.gov">Michael.Brady@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/WNB0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/WNB0.jpg" alt="William , Brownsberger">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/WNB0">William</a></td>
                                        <td><a href="/Legislators/Profile/WNB0">Brownsberger</a></td>
                                    <td>Suffolk and Middlesex</td>
                                    <td>Democrat</td>
                                    <td>319</td>
                                    <td>(617) 722-1280</td>
                                    <td>                                            <a href="mailto:William.Brownsberger@masenate.gov">William.Brownsberger@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/N_C0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/N_C0.jpg" alt="Nick , Collins">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/N_C0">Nick</a></td>
                                        <td><a href="/Legislators/Profile/N_C0">Collins</a></td>
                                    <td>First Suffolk</td>
                                    <td>Democrat</td>
                                    <td>312-E</td>
                                    <td>(617) 722-1150</td>
                                    <td>                                            <a href="mailto:Nick.Collins@masenate.gov">Nick.Collins@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JMC0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JMC0.jpg" alt="Joanne , Comerford">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JMC0">Joanne</a></td>
                                        <td><a href="/Legislators/Profile/JMC0">Comerford</a></td>
                                    <td>Hampshire, Franklin and Worcester</td>
                                    <td>Democrat</td>
                                    <td>410</td>
                                    <td>(617) 722-1532</td>
                                    <td>                                            <a href="mailto:Jo.Comerford@masenate.gov">Jo.Comerford@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CSC0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CSC0.jpg" alt="Cynthia , Creem">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CSC0">Cynthia</a></td>
                                        <td><a href="/Legislators/Profile/CSC0">Creem</a></td>
                                    <td>Norfolk and Middlesex</td>
                                    <td>Democrat</td>
                                    <td>312-A</td>
                                    <td>(617) 722-1639</td>
                                    <td>                                            <a href="mailto:Cynthia.Creem@masenate.gov">Cynthia.Creem@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BPC0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BPC0.jpg" alt="Brendan , Crighton">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BPC0">Brendan</a></td>
                                        <td><a href="/Legislators/Profile/BPC0">Crighton</a></td>
                                    <td>Third Essex</td>
                                    <td>Democrat</td>
                                    <td>109-C</td>
                                    <td>(617) 722-1350</td>
                                    <td>                                            <a href="mailto:brendan.crighton@masenate.gov">brendan.crighton@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JJC0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JJC0.jpg" alt="John , Cronin">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JJC0">John</a></td>
                                        <td><a href="/Legislators/Profile/JJC0">Cronin</a></td>
                                    <td>Worcester and Middlesex</td>
                                    <td>Democrat</td>
                                    <td>218</td>
                                    <td>(617) 722-1230</td>
                                    <td>                                            <a href="mailto:John.Cronin@masenate.gov">John.Cronin@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JAC0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JAC0.jpg" alt="Julian , Cyr">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JAC0">Julian</a></td>
                                        <td><a href="/Legislators/Profile/JAC0">Cyr</a></td>
                                    <td>Cape and Islands</td>
                                    <td>Democrat</td>
                                    <td>111</td>
                                    <td>(617) 722-1570</td>
                                    <td>                                            <a href="mailto:julian.cyr@masenate.gov">julian.cyr@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SND0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SND0.jpg" alt="Sal , DiDomenico">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SND0">Sal</a></td>
                                        <td><a href="/Legislators/Profile/SND0">DiDomenico</a></td>
                                    <td>Middlesex and Suffolk</td>
                                    <td>Democrat</td>
                                    <td>405</td>
                                    <td>(617) 722-1650</td>
                                    <td>                                            <a href="mailto:Sal.DiDomenico@masenate.gov">Sal.DiDomenico@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KAD0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KAD0.jpg" alt="Kelly , Dooner">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KAD0">Kelly</a></td>
                                        <td><a href="/Legislators/Profile/KAD0">Dooner</a></td>
                                    <td>Third Bristol and Plymouth</td>
                                    <td>Republican</td>
                                    <td>213-B</td>
                                    <td>(617) 722-1551</td>
                                    <td>                                            <a href="mailto:kelly.dooner@masenate.gov">kelly.dooner@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/WJD0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/WJD0.jpg" alt="William , Driscoll">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/WJD0">William</a></td>
                                        <td><a href="/Legislators/Profile/WJD0">Driscoll</a></td>
                                    <td>Norfolk, Plymouth and Bristol</td>
                                    <td>Democrat</td>
                                    <td>312-D</td>
                                    <td>(617) 722-1643</td>
                                    <td>                                            <a href="mailto:william.driscoll@masenate.gov">william.driscoll@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PJD0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PJD0.jpg" alt="Peter , Durant">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PJD0">Peter</a></td>
                                        <td><a href="/Legislators/Profile/PJD0">Durant</a></td>
                                    <td>Worcester and Hampshire</td>
                                    <td>Republican</td>
                                    <td>413-A</td>
                                    <td>(617) 722-1540</td>
                                    <td>                                            <a href="mailto:peter.durant@masenate.gov">peter.durant@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/LME0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/LME0.jpg" alt="Lydia , Edwards">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/LME0">Lydia</a></td>
                                        <td><a href="/Legislators/Profile/LME0">Edwards</a></td>
                                    <td>Third Suffolk</td>
                                    <td>Democrat</td>
                                    <td>413-C</td>
                                    <td>(617) 722-1634</td>
                                    <td>                                            <a href="mailto:Lydia.Edwards@masenate.gov">Lydia.Edwards@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JBE0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JBE0.jpg" alt="James , Eldridge">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JBE0">James</a></td>
                                        <td><a href="/Legislators/Profile/JBE0">Eldridge</a></td>
                                    <td>Middlesex and Worcester</td>
                                    <td>Democrat</td>
                                    <td>511-C</td>
                                    <td>(617) 722-1120</td>
                                    <td>                                            <a href="mailto:James.Eldridge@masenate.gov">James.Eldridge@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RCF0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RCF0.jpg" alt="Ryan , Fattman">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RCF0">Ryan</a></td>
                                        <td><a href="/Legislators/Profile/RCF0">Fattman</a></td>
                                    <td>Worcester and Hampden</td>
                                    <td>Republican</td>
                                    <td>213-A</td>
                                    <td>(617) 722-1420</td>
                                    <td>                                            <a href="mailto:Ryan.Fattman@masenate.gov">Ryan.Fattman@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PRF0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PRF0.jpg" alt="Paul , Feeney">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PRF0">Paul</a></td>
                                        <td><a href="/Legislators/Profile/PRF0">Feeney</a></td>
                                    <td>Bristol and Norfolk</td>
                                    <td>Democrat</td>
                                    <td>112</td>
                                    <td>(617) 722-1222</td>
                                    <td>                                            <a href="mailto:paul.feeney@masenate.gov">paul.feeney@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DAF0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DAF0.jpg" alt="Dylan , Fernandes">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DAF0">Dylan</a></td>
                                        <td><a href="/Legislators/Profile/DAF0">Fernandes</a></td>
                                    <td>Plymouth and Barnstable</td>
                                    <td>Democrat</td>
                                    <td>70</td>
                                    <td>(617) 722-1330</td>
                                    <td>                                            <a href="mailto:dylan.fernandes@masenate.gov">dylan.fernandes@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BRF0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BRF0.jpg" alt="Barry , Finegold">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BRF0">Barry</a></td>
                                        <td><a href="/Legislators/Profile/BRF0">Finegold</a></td>
                                    <td>Second Essex and Middlesex</td>
                                    <td>Democrat</td>
                                    <td>109-D</td>
                                    <td>(617) 722-1612</td>
                                    <td>                                            <a href="mailto:Barry.Finegold@masenate.gov">Barry.Finegold@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CFF0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CFF0.jpg" alt="Cindy , Friedman">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CFF0">Cindy</a></td>
                                        <td><a href="/Legislators/Profile/CFF0">Friedman</a></td>
                                    <td>Fourth Middlesex</td>
                                    <td>Democrat</td>
                                    <td>313</td>
                                    <td>(617) 722-1432</td>
                                    <td>                                            <a href="mailto:Cindy.Friedman@masenate.gov">Cindy.Friedman@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/A_G0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/A_G0.jpg" alt="Adam , Gomez">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/A_G0">Adam</a></td>
                                        <td><a href="/Legislators/Profile/A_G0">Gomez</a></td>
                                    <td>Hampden</td>
                                    <td>Democrat</td>
                                    <td>413-B</td>
                                    <td>(617) 722-1660</td>
                                    <td>                                            <a href="mailto:Adam.Gomez@masenate.gov">Adam.Gomez@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PDJ0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PDJ0.jpg" alt="Patricia , Jehlen">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PDJ0">Patricia</a></td>
                                        <td><a href="/Legislators/Profile/PDJ0">Jehlen</a></td>
                                    <td>Second Middlesex</td>
                                    <td>Democrat</td>
                                    <td>424</td>
                                    <td>(617) 722-1578</td>
                                    <td>                                            <a href="mailto:Patricia.Jehlen@masenate.gov">Patricia.Jehlen@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JFK0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JFK0.jpg" alt="John , Keenan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JFK0">John</a></td>
                                        <td><a href="/Legislators/Profile/JFK0">Keenan</a></td>
                                    <td>Norfolk and Plymouth</td>
                                    <td>Democrat</td>
                                    <td>413-F</td>
                                    <td>(617) 722-1494</td>
                                    <td>                                            <a href="mailto:John.Keenan@masenate.gov">John.Keenan@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/EDJ0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/EDJ0.jpg" alt="Edward , Kennedy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/EDJ0">Edward</a></td>
                                        <td><a href="/Legislators/Profile/EDJ0">Kennedy</a></td>
                                    <td>First Middlesex</td>
                                    <td>Democrat</td>
                                    <td>109-E</td>
                                    <td>(617) 722-1630</td>
                                    <td>                                            <a href="mailto:edward.kennedy@masenate.gov">edward.kennedy@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RKK0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RKK0.jpg" alt="Robyn , Kennedy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RKK0">Robyn</a></td>
                                        <td><a href="/Legislators/Profile/RKK0">Kennedy</a></td>
                                    <td>First Worcester</td>
                                    <td>Democrat</td>
                                    <td>507</td>
                                    <td>(617) 722-1544</td>
                                    <td>                                            <a href="mailto:Robyn.Kennedy@masenate.gov">Robyn.Kennedy@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/jml0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/jml0.jpg" alt="Jason , Lewis">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/jml0">Jason</a></td>
                                        <td><a href="/Legislators/Profile/jml0">Lewis</a></td>
                                    <td>Fifth Middlesex</td>
                                    <td>Democrat</td>
                                    <td>511-B</td>
                                    <td>(617) 722-1206</td>
                                    <td>                                            <a href="mailto:Jason.Lewis@masenate.gov">Jason.Lewis@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JBL0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JBL0.jpg" alt="Joan , Lovely">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JBL0">Joan</a></td>
                                        <td><a href="/Legislators/Profile/JBL0">Lovely</a></td>
                                    <td>Second Essex</td>
                                    <td>Democrat</td>
                                    <td>413-D</td>
                                    <td>(617) 722-1410</td>
                                    <td>                                            <a href="mailto:Joan.Lovely@masenate.gov">Joan.Lovely@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PWM0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PWM0.jpg" alt="Paul , Mark">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PWM0">Paul</a></td>
                                        <td><a href="/Legislators/Profile/PWM0">Mark</a></td>
                                    <td>Berkshire, Hampden, Franklin and Hampshire</td>
                                    <td>Democrat</td>
                                    <td>504</td>
                                    <td>(617) 722-1625</td>
                                    <td>                                            <a href="mailto:Paul.Mark@masenate.gov">Paul.Mark@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/L%20M0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/L%20M0.jpg" alt="Liz , Miranda">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/L%20M0">Liz</a></td>
                                        <td><a href="/Legislators/Profile/L%20M0">Miranda</a></td>
                                    <td>Second Suffolk</td>
                                    <td>Democrat</td>
                                    <td>519</td>
                                    <td>(617) 722-1673</td>
                                    <td>                                            <a href="mailto:Liz.Miranda@masenate.gov">Liz.Miranda@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MCM0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MCM0.jpg" alt="Mark , Montigny">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MCM0">Mark</a></td>
                                        <td><a href="/Legislators/Profile/MCM0">Montigny</a></td>
                                    <td>Second Bristol and Plymouth</td>
                                    <td>Democrat</td>
                                    <td>312-C</td>
                                    <td>(617) 722-1440</td>
                                    <td>                                            <a href="mailto:Mark.Montigny@masenate.gov">Mark.Montigny@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MOM0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MOM0.jpg" alt="Michael , Moore">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MOM0">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MOM0">Moore</a></td>
                                    <td>Second Worcester</td>
                                    <td>Democrat</td>
                                    <td>109-B</td>
                                    <td>(617) 722-1485</td>
                                    <td>                                            <a href="mailto:Michael.Moore@masenate.gov">Michael.Moore@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PMO">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PMO.jpg" alt="Patrick , O'Connor">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PMO">Patrick</a></td>
                                        <td><a href="/Legislators/Profile/PMO">O'Connor</a></td>
                                    <td>First Plymouth and Norfolk</td>
                                    <td>Republican</td>
                                    <td>419</td>
                                    <td>(617) 722-1646</td>
                                    <td>                                            <a href="mailto:Patrick.OConnor@masenate.gov">Patrick.OConnor@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JRO0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JRO0.jpg" alt="Jacob , Oliveira">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JRO0">Jacob</a></td>
                                        <td><a href="/Legislators/Profile/JRO0">Oliveira</a></td>
                                    <td>Hampden, Hampshire and Worcester</td>
                                    <td>Democrat</td>
                                    <td>416-B</td>
                                    <td>(617) 722-1291</td>
                                    <td>                                            <a href="mailto:Jacob.Oliveira@masenate.gov">Jacob.Oliveira@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PMP0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PMP0.jpg" alt="Pavel , Payano">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PMP0">Pavel</a></td>
                                        <td><a href="/Legislators/Profile/PMP0">Payano</a></td>
                                    <td>First Essex</td>
                                    <td>Democrat</td>
                                    <td>520</td>
                                    <td>(617) 722-1604</td>
                                    <td>                                            <a href="mailto:Pavel.Payano@masenate.gov">Pavel.Payano@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RLR0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RLR0.jpg" alt="Rebecca , Rausch">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RLR0">Rebecca</a></td>
                                        <td><a href="/Legislators/Profile/RLR0">Rausch</a></td>
                                    <td>Norfolk, Worcester and Middlesex</td>
                                    <td>Democrat</td>
                                    <td>215</td>
                                    <td>(617) 722-1555</td>
                                    <td>                                            <a href="mailto:Becca.Rausch@masenate.gov">Becca.Rausch@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJR0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJR0.jpg" alt="Michael , Rodrigues">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJR0">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MJR0">Rodrigues</a></td>
                                    <td>First Bristol and Plymouth</td>
                                    <td>Democrat</td>
                                    <td>212</td>
                                    <td>(617) 722-1114</td>
                                    <td>                                            <a href="mailto:Michael.Rodrigues@masenate.gov">Michael.Rodrigues@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MFR0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MFR0.jpg" alt="Michael , Rush">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MFR0">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MFR0">Rush</a></td>
                                    <td>Norfolk and Suffolk</td>
                                    <td>Democrat</td>
                                    <td>208</td>
                                    <td>(617) 722-1348</td>
                                    <td>                                            <a href="mailto:Mike.Rush@masenate.gov">Mike.Rush@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KES0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KES0.jpg" alt="Karen , Spilka">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KES0">Karen</a></td>
                                        <td><a href="/Legislators/Profile/KES0">Spilka</a></td>
                                    <td>Middlesex and Norfolk</td>
                                    <td>Democrat</td>
                                    <td>332</td>
                                    <td>(617) 722-1500</td>
                                    <td>                                            <a href="mailto:Karen.Spilka@masenate.gov">Karen.Spilka@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BET0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BET0.jpg" alt="Bruce , Tarr">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BET0">Bruce</a></td>
                                        <td><a href="/Legislators/Profile/BET0">Tarr</a></td>
                                    <td>First Essex and Middlesex</td>
                                    <td>Republican</td>
                                    <td>308</td>
                                    <td>(617) 722-1600</td>
                                    <td>                                            <a href="mailto:Bruce.Tarr@masenate.gov">Bruce.Tarr@masenate.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JCV0">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JCV0.jpg" alt="John , Velis">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JCV0">John</a></td>
                                        <td><a href="/Legislators/Profile/JCV0">Velis</a></td>
                                    <td>Hampden and Hampshire</td>
                                    <td>Democrat</td>
                                    <td>513</td>
                                    <td>(617) 722-1415</td>
                                    <td>                                            <a href="mailto:john.velis@masenate.gov">john.velis@masenate.gov</a>
</td>
                                </tr>
                                                        </tbody>
                        </table>
                        """


soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

table_data = []

headers = [header.text.strip() for header in table.find_all('th')]

rows = table.find_all('tr')[1:]  

for row in rows:
    columns = row.find_all('td')
    row_data = {}
    
    if len(columns) > 2:
        name_a_tag = columns[2].find('a') 
        if name_a_tag:
            row_data['profile_url'] = "https://malegislature.gov" + name_a_tag['href'] 
    for i, column in enumerate(columns):
        row_data[headers[i]] = column.text.strip()

    table_data.append(row_data)

json_data = json.dumps(table_data, indent=4)

with open('senate.json', 'w') as json_file:
    json_file.write(json_data)

print(json_data)