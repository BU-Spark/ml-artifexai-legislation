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
                                            <a href="/Legislators/Profile/J_A1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_A1.jpg" alt="James , Arciero">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_A1">James</a></td>
                                        <td><a href="/Legislators/Profile/J_A1">Arciero</a></td>
                                    <td>2nd Middlesex</td>
                                    <td>Democrat</td>
                                    <td>134</td>
                                    <td>(617) 722-2575</td>
                                    <td>                                            <a href="mailto:James.Arciero@mahouse.gov">James.Arciero@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JCD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JCD1.jpg" alt="James , Arena-DeRosa">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JCD1">James</a></td>
                                        <td><a href="/Legislators/Profile/JCD1">Arena-DeRosa</a></td>
                                    <td>8th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:James.Arena-DeRosa@mahouse.gov">James.Arena-DeRosa@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JBA1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JBA1.jpg" alt="Jennifer Balinsky , Armini">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JBA1">Jennifer Balinsky</a></td>
                                        <td><a href="/Legislators/Profile/JBA1">Armini</a></td>
                                    <td>8th Essex</td>
                                    <td>Democrat</td>
                                    <td>21</td>
                                    <td>(617) 722-2140</td>
                                    <td>                                            <a href="mailto:Jennifer.Armini@mahouse.gov">Jennifer.Armini@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SBA1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SBA1.jpg" alt="Shirley , Arriaga">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SBA1">Shirley</a></td>
                                        <td><a href="/Legislators/Profile/SBA1">Arriaga</a></td>
                                    <td>8th Hampden</td>
                                    <td>Democrat</td>
                                    <td>448</td>
                                    <td>(617) 722-2582</td>
                                    <td>                                            <a href="mailto:Shirley.Arriaga@mahouse.gov">Shirley.Arriaga@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BMA1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BMA1.jpg" alt="Brian , Ashe">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BMA1">Brian</a></td>
                                        <td><a href="/Legislators/Profile/BMA1">Ashe</a></td>
                                    <td>2nd Hampden</td>
                                    <td>Democrat</td>
                                    <td>160</td>
                                    <td>(617) 722-2304</td>
                                    <td>                                            <a href="mailto:Brian.Ashe@mahouse.gov">Brian.Ashe@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BJA1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BJA1.jpg" alt="Bruce , Ayers">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BJA1">Bruce</a></td>
                                        <td><a href="/Legislators/Profile/BJA1">Ayers</a></td>
                                    <td>1st Norfolk</td>
                                    <td>Democrat</td>
                                    <td>473-C</td>
                                    <td>(617) 722-2070</td>
                                    <td>                                            <a href="mailto:Bruce.Ayers@mahouse.gov">Bruce.Ayers@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MLB1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MLB1.jpg" alt="Michelle , Badger">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MLB1">Michelle</a></td>
                                        <td><a href="/Legislators/Profile/MLB1">Badger</a></td>
                                    <td>1st Plymouth</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7309</td>
                                    <td>                                            <a href="mailto:Michelle.Badger@mahouse.gov">Michelle.Badger@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CPB2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CPB2.jpg" alt="Christine , Barber">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CPB2">Christine</a></td>
                                        <td><a href="/Legislators/Profile/CPB2">Barber</a></td>
                                    <td>34th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Christine.Barber@mahouse.gov">Christine.Barber@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/J_B1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_B1.jpg" alt="John , Barrett">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_B1">John</a></td>
                                        <td><a href="/Legislators/Profile/J_B1">Barrett</a></td>
                                    <td>1st Berkshire</td>
                                    <td>Democrat</td>
                                    <td>185</td>
                                    <td>(617) 722-2960</td>
                                    <td>                                            <a href="mailto:john.barrett@mahouse.gov">john.barrett@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DRB1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DRB1.jpg" alt="Donald , Berthiaume">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DRB1">Donald</a></td>
                                        <td><a href="/Legislators/Profile/DRB1">Berthiaume</a></td>
                                    <td>5th Worcester</td>
                                    <td>Republican</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:Donald.Berthiaume@mahouse.gov">Donald.Berthiaume@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/D_B1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/D_B1.jpg" alt="David , Biele">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/D_B1">David</a></td>
                                        <td><a href="/Legislators/Profile/D_B1">Biele</a></td>
                                    <td>4th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:David.Biele@mahouse.gov">David.Biele@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/NMB1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/NMB1.jpg" alt="Natalie , Blais">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/NMB1">Natalie</a></td>
                                        <td><a href="/Legislators/Profile/NMB1">Blais</a></td>
                                    <td>1st Franklin</td>
                                    <td>Democrat</td>
                                    <td>473</td>
                                    <td>(413) 362-9453</td>
                                    <td>                                            <a href="mailto:Natalie.Blais@mahouse.gov">Natalie.Blais@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/NAG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/NAG1.jpg" alt="Nicholas , Boldyga">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/NAG1">Nicholas</a></td>
                                        <td><a href="/Legislators/Profile/NAG1">Boldyga</a></td>
                                    <td>3rd Hampden</td>
                                    <td>Republican</td>
                                    <td>167</td>
                                    <td>(413) 274-8084</td>
                                    <td>                                            <a href="mailto:Nicholas.Boldyga@mahouse.gov">Nicholas.Boldyga@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AFC1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AFC1.jpg" alt="Antonio , Cabral">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AFC1">Antonio</a></td>
                                        <td><a href="/Legislators/Profile/AFC1">Cabral</a></td>
                                    <td>13th Bristol</td>
                                    <td>Democrat</td>
                                    <td>466</td>
                                    <td>(617) 722-2017</td>
                                    <td>                                            <a href="mailto:Antonio.Cabral@mahouse.gov">Antonio.Cabral@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DFC1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DFC1.jpg" alt="Daniel , Cahill">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DFC1">Daniel</a></td>
                                        <td><a href="/Legislators/Profile/DFC1">Cahill</a></td>
                                    <td>10th Essex</td>
                                    <td>Democrat</td>
                                    <td>527A</td>
                                    <td>(617) 722-2020</td>
                                    <td>                                            <a href="mailto:Daniel.Cahill@mahouse.gov">Daniel.Cahill@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/S_C1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/S_C1.jpg" alt="Simon , Cataldo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/S_C1">Simon</a></td>
                                        <td><a href="/Legislators/Profile/S_C1">Cataldo</a></td>
                                    <td>14th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>136</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Simon.Cataldo@mahouse.gov">Simon.Cataldo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MSC1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MSC1.jpg" alt="Michael , Chaisson">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MSC1">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MSC1">Chaisson</a></td>
                                    <td>1st Bristol</td>
                                    <td>Republican</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7308</td>
                                    <td>                                            <a href="mailto:Michael.Chaisson@mahouse.gov">Michael.Chaisson@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/T_C1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/T_C1.jpg" alt="Tackey , Chan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/T_C1">Tackey</a></td>
                                        <td><a href="/Legislators/Profile/T_C1">Chan</a></td>
                                    <td>2nd Norfolk</td>
                                    <td>Democrat</td>
                                    <td>42</td>
                                    <td>(617) 722-2370</td>
                                    <td>                                            <a href="mailto:Tackey.Chan@mahouse.gov">Tackey.Chan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/M_C2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/M_C2.jpg" alt="Michelle , Ciccolo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/M_C2">Michelle</a></td>
                                        <td><a href="/Legislators/Profile/M_C2">Ciccolo</a></td>
                                    <td>15th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473F</td>
                                    <td>(617) 722-2210</td>
                                    <td>                                            <a href="mailto:michelle.ciccolo@mahouse.gov">michelle.ciccolo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/M_C1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/M_C1.jpg" alt="Mike , Connolly">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/M_C1">Mike</a></td>
                                        <td><a href="/Legislators/Profile/M_C1">Connolly</a></td>
                                    <td>26th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>156</td>
                                    <td>(617) 722-2240</td>
                                    <td>                                            <a href="mailto:Mike.Connolly@mahouse.gov">Mike.Connolly@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/R_C1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/R_C1.jpg" alt="Rob , Consalvo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/R_C1">Rob</a></td>
                                        <td><a href="/Legislators/Profile/R_C1">Consalvo</a></td>
                                    <td>14th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>166</td>
                                    <td>(617) 722-2030</td>
                                    <td>                                            <a href="mailto:Rob.Consalvo@mahouse.gov">Rob.Consalvo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/M_C3">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/M_C3.jpg" alt="Manny , Cruz">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/M_C3">Manny</a></td>
                                        <td><a href="/Legislators/Profile/M_C3">Cruz</a></td>
                                    <td>7th Essex</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2011</td>
                                    <td>                                            <a href="mailto:Manny.Cruz@mahouse.gov">Manny.Cruz@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJC1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJC1.jpg" alt="Mark , Cusack">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJC1">Mark</a></td>
                                        <td><a href="/Legislators/Profile/MJC1">Cusack</a></td>
                                    <td>5th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>43</td>
                                    <td>(617) 722-2320</td>
                                    <td>                                            <a href="mailto:Mark.Cusack@mahouse.gov">Mark.Cusack@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/LSD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/LSD1.jpg" alt="Leigh , Davis">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/LSD1">Leigh</a></td>
                                        <td><a href="/Legislators/Profile/LSD1">Davis</a></td>
                                    <td>3rd Berkshire</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(413) 854-4623</td>
                                    <td>                                            <a href="mailto:Leigh.Davis@mahouse.gov">Leigh.Davis@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MSD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MSD1.jpg" alt="Michael , Day">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MSD1">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MSD1">Day</a></td>
                                    <td>31st Middlesex</td>
                                    <td>Democrat</td>
                                    <td>136</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Michael.Day@mahouse.gov">Michael.Day@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MCD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MCD1.jpg" alt="Marjorie , Decker">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MCD1">Marjorie</a></td>
                                        <td><a href="/Legislators/Profile/MCD1">Decker</a></td>
                                    <td>25th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>130</td>
                                    <td>(617) 722-2130</td>
                                    <td>                                            <a href="mailto:Marjorie.Decker@mahouse.gov">Marjorie.Decker@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DFD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DFD1.jpg" alt="David , DeCoste">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DFD1">David</a></td>
                                        <td><a href="/Legislators/Profile/DFD1">DeCoste</a></td>
                                    <td>5th Plymouth</td>
                                    <td>Republican</td>
                                    <td>542</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:David.DeCoste@mahouse.gov">David.DeCoste@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KAD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KAD1.jpg" alt="Kip , Diggs">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KAD1">Kip</a></td>
                                        <td><a href="/Legislators/Profile/KAD1">Diggs</a></td>
                                    <td>2nd Barnstable</td>
                                    <td>Democrat</td>
                                    <td>472</td>
                                    <td>(617) 722-2013</td>
                                    <td>                                            <a href="mailto:Kip.Diggs@mahouse.gov">Kip.Diggs@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/M_D2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/M_D2.jpg" alt="Mindy , Domb">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/M_D2">Mindy</a></td>
                                        <td><a href="/Legislators/Profile/M_D2">Domb</a></td>
                                    <td>3rd Hampshire</td>
                                    <td>Democrat</td>
                                    <td>174</td>
                                    <td>(617) 722-2877</td>
                                    <td>                                            <a href="mailto:mindy.domb@mahouse.gov">mindy.domb@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/K_D1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/K_D1.jpg" alt="Kate , Donaghue">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/K_D1">Kate</a></td>
                                        <td><a href="/Legislators/Profile/K_D1">Donaghue</a></td>
                                    <td>19th Worcester</td>
                                    <td>Democrat</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:Kate.Donaghue@mahouse.gov">Kate.Donaghue@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DMD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DMD1.jpg" alt="Daniel , Donahue">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DMD1">Daniel</a></td>
                                        <td><a href="/Legislators/Profile/DMD1">Donahue</a></td>
                                    <td>16th Worcester</td>
                                    <td>Democrat</td>
                                    <td>544</td>
                                    <td>(617) 722-2637</td>
                                    <td>                                            <a href="mailto:Daniel.Donahue@mahouse.gov">Daniel.Donahue@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PJD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PJD1.jpg" alt="Paul , Donato">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PJD1">Paul</a></td>
                                        <td><a href="/Legislators/Profile/PJD1">Donato</a></td>
                                    <td>35th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>478</td>
                                    <td>(617) 722-2520</td>
                                    <td>                                            <a href="mailto:Paul.Donato@mahouse.gov">Paul.Donato@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MMD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MMD1.jpg" alt="Michelle , DuBois">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MMD1">Michelle</a></td>
                                        <td><a href="/Legislators/Profile/MMD1">DuBois</a></td>
                                    <td>10th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>466</td>
                                    <td>(617) 722-2017</td>
                                    <td>                                            <a href="mailto:Michelle.DuBois@MAHouse.gov">Michelle.DuBois@MAHouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PAD1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PAD1.jpg" alt="Patricia , Duffy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PAD1">Patricia</a></td>
                                        <td><a href="/Legislators/Profile/PAD1">Duffy</a></td>
                                    <td>5th Hampden</td>
                                    <td>Democrat</td>
                                    <td>544</td>
                                    <td>(617) 722-2637</td>
                                    <td>                                            <a href="mailto:Patricia.Duffy@mahouse.gov">Patricia.Duffy@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RME1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RME1.jpg" alt="Rodney , Elliott">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RME1">Rodney</a></td>
                                        <td><a href="/Legislators/Profile/RME1">Elliott</a></td>
                                    <td>16th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>26</td>
                                    <td>(617) 722-2080</td>
                                    <td>                                            <a href="mailto:Rodney.Elliott@mahouse.gov">Rodney.Elliott@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TFB1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TFB1.jpg" alt="Tricia , Farley-Bouvier">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TFB1">Tricia</a></td>
                                        <td><a href="/Legislators/Profile/TFB1">Farley-Bouvier</a></td>
                                    <td>2nd Berkshire</td>
                                    <td>Democrat</td>
                                    <td>274</td>
                                    <td>(617) 722-2676</td>
                                    <td>                                            <a href="mailto:Tricia.Farley-Bouvier@mahouse.gov">Tricia.Farley-Bouvier@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KNF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KNF1.jpg" alt="Kimberly , Ferguson">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KNF1">Kimberly</a></td>
                                        <td><a href="/Legislators/Profile/KNF1">Ferguson</a></td>
                                    <td>1st Worcester</td>
                                    <td>Republican</td>
                                    <td>124</td>
                                    <td>(617) 722-2100</td>
                                    <td>                                            <a href="mailto:Kimberly.Ferguson@mahouse.gov">Kimberly.Ferguson@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AMF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AMF1.jpg" alt="Ann-Margaret , Ferrante">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AMF1">Ann-Margaret</a></td>
                                        <td><a href="/Legislators/Profile/AMF1">Ferrante</a></td>
                                    <td>5th Essex</td>
                                    <td>Democrat</td>
                                    <td>238</td>
                                    <td>(617) 722-2380</td>
                                    <td>                                            <a href="mailto:Ann-Margaret.Ferrante@mahouse.gov">Ann-Margaret.Ferrante@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJF1.jpg" alt="Michael , Finn">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJF1">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MJF1">Finn</a></td>
                                    <td>6th Hampden</td>
                                    <td>Democrat</td>
                                    <td>42</td>
                                    <td>(617) 722-2014</td>
                                    <td>                                            <a href="mailto:Michael.Finn@mahouse.gov">Michael.Finn@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CAF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CAF1.jpg" alt="Carole , Fiola">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CAF1">Carole</a></td>
                                        <td><a href="/Legislators/Profile/CAF1">Fiola</a></td>
                                    <td>6th Bristol</td>
                                    <td>Democrat</td>
                                    <td>236</td>
                                    <td>(617) 722-2430</td>
                                    <td>                                            <a href="mailto:Carole.Fiola@mahouse.gov">Carole.Fiola@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CRF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CRF1.jpg" alt="Christopher , Flanagan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CRF1">Christopher</a></td>
                                        <td><a href="/Legislators/Profile/CRF1">Flanagan</a></td>
                                    <td>1st Barnstable</td>
                                    <td>Democrat</td>
                                    <td>26</td>
                                    <td>(617) 722-2080</td>
                                    <td>                                            <a href="mailto:Christopher.Flanagan@mahouse.gov">Christopher.Flanagan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BFO1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BFO1.jpg" alt="Brandy , Fluker-Reid">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BFO1">Brandy</a></td>
                                        <td><a href="/Legislators/Profile/BFO1">Fluker-Reid</a></td>
                                    <td>12th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>136</td>
                                    <td>(617) 722-2430</td>
                                    <td>                                            <a href="mailto:Brandy.FlukerReid@mahouse.gov">Brandy.FlukerReid@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PKF1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PKF1.jpg" alt="Paul , Frost">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PKF1">Paul</a></td>
                                        <td><a href="/Legislators/Profile/PKF1">Frost</a></td>
                                    <td>7th Worcester</td>
                                    <td>Republican</td>
                                    <td>124</td>
                                    <td>(617) 722-2100</td>
                                    <td>                                            <a href="mailto:Paul.Frost@mahouse.gov">Paul.Frost@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DCG2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DCG2.jpg" alt="Dennis , Gallagher">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DCG2">Dennis</a></td>
                                        <td><a href="/Legislators/Profile/DCG2">Gallagher</a></td>
                                    <td>8th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7306</td>
                                    <td>                                            <a href="mailto:Dennis.Gallagher@mahouse.gov">Dennis.Gallagher@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/WCG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/WCG1.jpg" alt="William , Galvin">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/WCG1">William</a></td>
                                        <td><a href="/Legislators/Profile/WCG1">Galvin</a></td>
                                    <td>6th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>166</td>
                                    <td>(617) 722-2692</td>
                                    <td>                                            <a href="mailto:William.Galvin@mahouse.gov">William.Galvin@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/S_G1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/S_G1.jpg" alt="Sean , Garballey">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/S_G1">Sean</a></td>
                                        <td><a href="/Legislators/Profile/S_G1">Garballey</a></td>
                                    <td>23rd Middlesex</td>
                                    <td>Democrat</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:Sean.Garballey@mahouse.gov">Sean.Garballey@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JAG2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JAG2.jpg" alt="Judith , Garcia">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JAG2">Judith</a></td>
                                        <td><a href="/Legislators/Profile/JAG2">Garcia</a></td>
                                    <td>11th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2011</td>
                                    <td>                                            <a href="mailto:Judith.Garcia@mahouse.gov">Judith.Garcia@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CMG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CMG1.jpg" alt="Colleen , Garry">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CMG1">Colleen</a></td>
                                        <td><a href="/Legislators/Profile/CMG1">Garry</a></td>
                                    <td>36th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>238</td>
                                    <td>(617) 722-2380</td>
                                    <td>                                            <a href="mailto:Colleen.Garry@mahouse.gov">Colleen.Garry@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JRG2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JRG2.jpg" alt="John , Gaskey">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JRG2">John</a></td>
                                        <td><a href="/Legislators/Profile/JRG2">Gaskey</a></td>
                                    <td>2nd Plymouth</td>
                                    <td>Republican</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7305</td>
                                    <td>                                            <a href="mailto:John.Gaskey@mahouse.gov">John.Gaskey@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CLG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CLG1.jpg" alt="Carmine , Gentile">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CLG1">Carmine</a></td>
                                        <td><a href="/Legislators/Profile/CLG1">Gentile</a></td>
                                    <td>13th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:carmine.gentile@mahouse.gov">carmine.gentile@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JAG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JAG1.jpg" alt="Jessica , Giannino">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JAG1">Jessica</a></td>
                                        <td><a href="/Legislators/Profile/JAG1">Giannino</a></td>
                                    <td>16th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2011</td>
                                    <td>                                            <a href="mailto:Jessica.Giannino@mahouse.gov">Jessica.Giannino@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/H_G1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/H_G1.jpg" alt="Homar , Gómez">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/H_G1">Homar</a></td>
                                        <td><a href="/Legislators/Profile/H_G1">Gómez</a></td>
                                    <td>2nd Hampshire</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(413) 977-2676</td>
                                    <td>                                            <a href="mailto:Homar.Gomez@mahouse.gov">Homar.Gomez@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/C_G1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/C_G1.jpg" alt="Carlos , González">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/C_G1">Carlos</a></td>
                                        <td><a href="/Legislators/Profile/C_G1">González</a></td>
                                    <td>10th Hampden</td>
                                    <td>Democrat</td>
                                    <td>163</td>
                                    <td>(617) 722-2199</td>
                                    <td>                                            <a href="mailto:Carlos.Gonzalez@mahouse.gov">Carlos.Gonzalez@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KIG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KIG1.jpg" alt="Kenneth , Gordon">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KIG1">Kenneth</a></td>
                                        <td><a href="/Legislators/Profile/KIG1">Gordon</a></td>
                                    <td>21st Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473G</td>
                                    <td>(617) 722-2070</td>
                                    <td>                                            <a href="mailto:Ken.Gordon@mahouse.gov">Ken.Gordon@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DWG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DWG1.jpg" alt="Danielle , Gregoire">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DWG1">Danielle</a></td>
                                        <td><a href="/Legislators/Profile/DWG1">Gregoire</a></td>
                                    <td>4th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>21</td>
                                    <td>(617) 722-2140</td>
                                    <td>                                            <a href="mailto:Danielle.Gregoire@mahouse.gov">Danielle.Gregoire@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RMH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RMH1.jpg" alt="Richard , Haggerty">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RMH1">Richard</a></td>
                                        <td><a href="/Legislators/Profile/RMH1">Haggerty</a></td>
                                    <td>30th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2080</td>
                                    <td>                                            <a href="mailto:richard.haggerty@mahouse.gov">richard.haggerty@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RMH2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RMH2.jpg" alt="Ryan , Hamilton">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RMH2">Ryan</a></td>
                                        <td><a href="/Legislators/Profile/RMH2">Hamilton</a></td>
                                    <td>15th Essex</td>
                                    <td>Democrat</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:Ryan.Hamilton@mahouse.gov">Ryan.Hamilton@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JKH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JKH1.jpg" alt="James , Hawkins">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JKH1">James</a></td>
                                        <td><a href="/Legislators/Profile/JKH1">Hawkins</a></td>
                                    <td>2nd Bristol</td>
                                    <td>Democrat</td>
                                    <td>472</td>
                                    <td>(617) 722-2013</td>
                                    <td>                                            <a href="mailto:james.hawkins@mahouse.gov">james.hawkins@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/C_H1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/C_H1.jpg" alt="Christopher , Hendricks">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/C_H1">Christopher</a></td>
                                        <td><a href="/Legislators/Profile/C_H1">Hendricks</a></td>
                                    <td>11th Bristol</td>
                                    <td>Democrat</td>
                                    <td>26</td>
                                    <td>(617) 722-2305</td>
                                    <td>                                            <a href="mailto:Chris.Hendricks@mahouse.gov">Chris.Hendricks@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/N_H1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/N_H1.jpg" alt="Natalie , Higgins">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/N_H1">Natalie</a></td>
                                        <td><a href="/Legislators/Profile/N_H1">Higgins</a></td>
                                    <td>4th Worcester</td>
                                    <td>Democrat</td>
                                    <td>39</td>
                                    <td>(617) 722-2014</td>
                                    <td>                                            <a href="mailto:Natalie.Higgins@mahouse.gov">Natalie.Higgins@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/K_H1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/K_H1.jpg" alt="Kate , Hogan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/K_H1">Kate</a></td>
                                        <td><a href="/Legislators/Profile/K_H1">Hogan</a></td>
                                    <td>3rd Middlesex</td>
                                    <td>Democrat</td>
                                    <td>370</td>
                                    <td>(617) 722-2600</td>
                                    <td>                                            <a href="mailto:Kate.Hogan@mahouse.gov">Kate.Hogan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/REH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/REH1.jpg" alt="Russell , Holmes">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/REH1">Russell</a></td>
                                        <td><a href="/Legislators/Profile/REH1">Holmes</a></td>
                                    <td>6th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>254</td>
                                    <td>(617) 722-2220</td>
                                    <td>                                            <a href="mailto:Russell.Holmes@mahouse.gov">Russell.Holmes@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KGH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KGH1.jpg" alt="Kevin , Honan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KGH1">Kevin</a></td>
                                        <td><a href="/Legislators/Profile/KGH1">Honan</a></td>
                                    <td>17th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>38</td>
                                    <td>(617) 722-2470</td>
                                    <td>                                            <a href="mailto:Kevin.Honan@mahouse.gov">Kevin.Honan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TTH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TTH1.jpg" alt="Tara , Hong">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TTH1">Tara</a></td>
                                        <td><a href="/Legislators/Profile/TTH1">Hong</a></td>
                                    <td>18th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7310</td>
                                    <td>                                            <a href="mailto:Tara.Hong@mahouse.gov">Tara.Hong@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/V_H1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/V_H1.jpg" alt="Vanna , Howard">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/V_H1">Vanna</a></td>
                                        <td><a href="/Legislators/Profile/V_H1">Howard</a></td>
                                    <td>17th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:Vanna.Howard@mahouse.gov">Vanna.Howard@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SSH1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SSH1.jpg" alt="Steven , Howitt">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SSH1">Steven</a></td>
                                        <td><a href="/Legislators/Profile/SSH1">Howitt</a></td>
                                    <td>4th Bristol</td>
                                    <td>Republican</td>
                                    <td>237</td>
                                    <td>(617) 722-2305</td>
                                    <td>                                            <a href="mailto:Steven.Howitt@mahouse.gov">Steven.Howitt@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/djh1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/djh1.jpg" alt="Daniel , Hunt">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/djh1">Daniel</a></td>
                                        <td><a href="/Legislators/Profile/djh1">Hunt</a></td>
                                    <td>13th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Daniel.Hunt@mahouse.gov">Daniel.Hunt@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BHJ1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BHJ1.jpg" alt="Bradley , Jones">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BHJ1">Bradley</a></td>
                                        <td><a href="/Legislators/Profile/BHJ1">Jones</a></td>
                                    <td>20th Middlesex</td>
                                    <td>Republican</td>
                                    <td>124</td>
                                    <td>(617) 722-2100</td>
                                    <td>                                            <a href="mailto:Bradley.Jones@mahouse.gov">Bradley.Jones@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/HEK1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/HEK1.jpg" alt="Hannah , Kane">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/HEK1">Hannah</a></td>
                                        <td><a href="/Legislators/Profile/HEK1">Kane</a></td>
                                    <td>11th Worcester</td>
                                    <td>Republican</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:Hannah.Kane@mahouse.gov">Hannah.Kane@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/K_K2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/K_K2.jpg" alt="Kristin , Kassner">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/K_K2">Kristin</a></td>
                                        <td><a href="/Legislators/Profile/K_K2">Kassner</a></td>
                                    <td>2nd Essex</td>
                                    <td>Democrat</td>
                                    <td>130</td>
                                    <td>(617) 722-2000 x7905</td>
                                    <td>                                            <a href="mailto:Kristin.Kassner@mahouse.gov">Kristin.Kassner@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PJK1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PJK1.jpg" alt="Patrick , Kearney">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PJK1">Patrick</a></td>
                                        <td><a href="/Legislators/Profile/PJK1">Kearney</a></td>
                                    <td>4th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>39</td>
                                    <td>(617) 722-2014</td>
                                    <td>                                            <a href="mailto:patrick.kearney@mahouse.gov">patrick.kearney@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MSK1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MSK1.jpg" alt="Mary , Keefe">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MSK1">Mary</a></td>
                                        <td><a href="/Legislators/Profile/MSK1">Keefe</a></td>
                                    <td>15th Worcester</td>
                                    <td>Democrat</td>
                                    <td>466</td>
                                    <td>(617) 722-2017</td>
                                    <td>                                            <a href="mailto:Mary.Keefe@mahouse.gov">Mary.Keefe@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SPK1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SPK1.jpg" alt="Sally , Kerans">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SPK1">Sally</a></td>
                                        <td><a href="/Legislators/Profile/SPK1">Kerans</a></td>
                                    <td>13th Essex</td>
                                    <td>Democrat</td>
                                    <td>473F</td>
                                    <td>(617) 722-2210</td>
                                    <td>                                            <a href="mailto:Sally.Kerans@mahouse.gov">Sally.Kerans@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/M_K1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/M_K1.jpg" alt="Meghan , Kilcoyne">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/M_K1">Meghan</a></td>
                                        <td><a href="/Legislators/Profile/M_K1">Kilcoyne</a></td>
                                    <td>12th Worcester</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:meghan.kilcoyne@mahouse.gov">meghan.kilcoyne@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MPK1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MPK1.jpg" alt="Michael , Kushmerek">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MPK1">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MPK1">Kushmerek</a></td>
                                    <td>3rd Worcester</td>
                                    <td>Democrat</td>
                                    <td>136</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Michael.Kushmerek@mahouse.gov">Michael.Kushmerek@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KPL1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KPL1.jpg" alt="Kathleen , LaNatra">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KPL1">Kathleen</a></td>
                                        <td><a href="/Legislators/Profile/KPL1">LaNatra</a></td>
                                    <td>12th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>42</td>
                                    <td>(617) 722-2575</td>
                                    <td>                                            <a href="mailto:kathleen.lanatra@mahouse.gov">kathleen.lanatra@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JJL2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JJL2.jpg" alt="John , Lawn">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JJL2">John</a></td>
                                        <td><a href="/Legislators/Profile/JJL2">Lawn</a></td>
                                    <td>10th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>236</td>
                                    <td>(617) 722-2430</td>
                                    <td>                                            <a href="mailto:John.Lawn@mahouse.gov">John.Lawn@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DAL1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DAL1.jpg" alt="David , LeBoeuf">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DAL1">David</a></td>
                                        <td><a href="/Legislators/Profile/DAL1">LeBoeuf</a></td>
                                    <td>17th Worcester</td>
                                    <td>Democrat</td>
                                    <td>237</td>
                                    <td>(617) 722-2305</td>
                                    <td>                                            <a href="mailto:david.leboeuf@mahouse.gov">david.leboeuf@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JPL1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JPL1.jpg" alt="Jack , Lewis">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JPL1">Jack</a></td>
                                        <td><a href="/Legislators/Profile/JPL1">Lewis</a></td>
                                    <td>7th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>452</td>
                                    <td>(617) 722-2582</td>
                                    <td>                                            <a href="mailto:Jack.Lewis@mahouse.gov">Jack.Lewis@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DPL1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DPL1.jpg" alt="David , Linsky">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DPL1">David</a></td>
                                        <td><a href="/Legislators/Profile/DPL1">Linsky</a></td>
                                    <td>5th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:David.Linsky@mahouse.gov">David.Linsky@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KLG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KLG1.jpg" alt="Kate , Lipper-Garabedian">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KLG1">Kate</a></td>
                                        <td><a href="/Legislators/Profile/KLG1">Lipper-Garabedian</a></td>
                                    <td>32nd Middlesex</td>
                                    <td>Democrat</td>
                                    <td>185</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:kate.lipper-garabedian@mahouse.gov">kate.lipper-garabedian@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/J_L1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_L1.jpg" alt="Jay , Livingstone">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_L1">Jay</a></td>
                                        <td><a href="/Legislators/Profile/J_L1">Livingstone</a></td>
                                    <td>8th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2011</td>
                                    <td>                                            <a href="mailto:Jay.Livingstone@mahouse.gov">Jay.Livingstone@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MTL1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MTL1.jpg" alt="Marc , Lombardo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MTL1">Marc</a></td>
                                        <td><a href="/Legislators/Profile/MTL1">Lombardo</a></td>
                                    <td>22nd Middlesex</td>
                                    <td>Republican</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Marc.Lombardo@mahouse.gov">Marc.Lombardo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/H_L1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/H_L1.jpg" alt="Hadley , Luddy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/H_L1">Hadley</a></td>
                                        <td><a href="/Legislators/Profile/H_L1">Luddy</a></td>
                                    <td>4th Barnstable</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7313</td>
                                    <td>                                            <a href="mailto:Hadley.Luddy@mahouse.gov">Hadley.Luddy@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/WFM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/WFM1.jpg" alt="William , MacGregor">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/WFM1">William</a></td>
                                        <td><a href="/Legislators/Profile/WFM1">MacGregor</a></td>
                                    <td>10th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:bill.macgregor@mahouse.gov">bill.macgregor@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/ACM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/ACM1.jpg" alt="Adrian , Madaro">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/ACM1">Adrian</a></td>
                                        <td><a href="/Legislators/Profile/ACM1">Madaro</a></td>
                                    <td>1st Suffolk</td>
                                    <td>Democrat</td>
                                    <td>34</td>
                                    <td>(617) 722-2320</td>
                                    <td>                                            <a href="mailto:Adrian.Madaro@mahouse.gov">Adrian.Madaro@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JJM2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JJM2.jpg" alt="John , Mahoney">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JJM2">John</a></td>
                                        <td><a href="/Legislators/Profile/JJM2">Mahoney</a></td>
                                    <td>13th Worcester</td>
                                    <td>Democrat</td>
                                    <td>146</td>
                                    <td>(617) 722-2575</td>
                                    <td>                                            <a href="mailto:John.Mahoney@mahouse.gov">John.Mahoney@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/R_M1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/R_M1.jpg" alt="Ronald , Mariano">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/R_M1">Ronald</a></td>
                                        <td><a href="/Legislators/Profile/R_M1">Mariano</a></td>
                                    <td>3rd Norfolk</td>
                                    <td>Democrat</td>
                                    <td>356</td>
                                    <td>(617) 722-2500</td>
                                    <td>                                            <a href="mailto:Ronald.Mariano@mahouse.gov">Ronald.Mariano@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CMM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CMM1.jpg" alt="Christopher , Markey">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CMM1">Christopher</a></td>
                                        <td><a href="/Legislators/Profile/CMM1">Markey</a></td>
                                    <td>9th Bristol</td>
                                    <td>Democrat</td>
                                    <td>276</td>
                                    <td>(617) 722-2676</td>
                                    <td>                                            <a href="mailto:Christopher.Markey@mahouse.gov">Christopher.Markey@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JJM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JJM1.jpg" alt="John , Marsi">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JJM1">John</a></td>
                                        <td><a href="/Legislators/Profile/JJM1">Marsi</a></td>
                                    <td>6th Worcester</td>
                                    <td>Republican</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:John.Marsi@mahouse.gov">John.Marsi@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/jwm1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/jwm1.jpg" alt="Joseph , McGonagle">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/jwm1">Joseph</a></td>
                                        <td><a href="/Legislators/Profile/jwm1">McGonagle</a></td>
                                    <td>28th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>277</td>
                                    <td>(617) 722-2012</td>
                                    <td>                                            <a href="mailto:Joseph.McGonagle@mahouse.gov">Joseph.McGonagle@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JDM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JDM1.jpg" alt="Joseph , McKenna">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JDM1">Joseph</a></td>
                                        <td><a href="/Legislators/Profile/JDM1">McKenna</a></td>
                                    <td>18th Worcester</td>
                                    <td>Republican</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:joseph.mckenna@mahouse.gov">joseph.mckenna@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/P_M1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/P_M1.jpg" alt="Paul , McMurtry">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/P_M1">Paul</a></td>
                                        <td><a href="/Legislators/Profile/P_M1">McMurtry</a></td>
                                    <td>11th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>26</td>
                                    <td>(617) 722-2080</td>
                                    <td>                                            <a href="mailto:Paul.McMurtry@mahouse.gov">Paul.McMurtry@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RAM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RAM1.jpg" alt="Rita , Mendes">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RAM1">Rita</a></td>
                                        <td><a href="/Legislators/Profile/RAM1">Mendes</a></td>
                                    <td>11th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>134</td>
                                    <td>(617) 722-2400</td>
                                    <td>                                            <a href="mailto:Rita.Mendes@mahouse.gov">Rita.Mendes@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/J_M1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_M1.jpg" alt="Joan , Meschino">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_M1">Joan</a></td>
                                        <td><a href="/Legislators/Profile/J_M1">Meschino</a></td>
                                    <td>3rd Plymouth</td>
                                    <td>Democrat</td>
                                    <td>162</td>
                                    <td>(617) 722-2092</td>
                                    <td>                                            <a href="mailto:Joan.Meschino@mahouse.gov">Joan.Meschino@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AMM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AMM1.jpg" alt="Aaron , Michlewitz">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AMM1">Aaron</a></td>
                                        <td><a href="/Legislators/Profile/AMM1">Michlewitz</a></td>
                                    <td>3rd Suffolk</td>
                                    <td>Democrat</td>
                                    <td>243</td>
                                    <td>(617) 722-2990</td>
                                    <td>                                            <a href="mailto:Aaron.M.Michlewitz@mahouse.gov">Aaron.M.Michlewitz@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TWM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TWM1.jpg" alt="Thomas , Moakley">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TWM1">Thomas</a></td>
                                        <td><a href="/Legislators/Profile/TWM1">Moakley</a></td>
                                    <td>Barnstable, Dukes and Nantucket</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7302</td>
                                    <td>                                            <a href="mailto:Thomas.Moakley@mahouse.gov">Thomas.Moakley@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/S_M1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/S_M1.jpg" alt="Samantha , Montaño">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/S_M1">Samantha</a></td>
                                        <td><a href="/Legislators/Profile/S_M1">Montaño</a></td>
                                    <td>15th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>446</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Samantha.Montano@mahouse.gov">Samantha.Montano@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/FAM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/FAM1.jpg" alt="Frank , Moran">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/FAM1">Frank</a></td>
                                        <td><a href="/Legislators/Profile/FAM1">Moran</a></td>
                                    <td>17th Essex</td>
                                    <td>Democrat</td>
                                    <td>481</td>
                                    <td>(617) 722-2180</td>
                                    <td>                                            <a href="mailto:Frank.Moran@mahouse.gov">Frank.Moran@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JFM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JFM1.jpg" alt="John , Moran">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JFM1">John</a></td>
                                        <td><a href="/Legislators/Profile/JFM1">Moran</a></td>
                                    <td>9th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:john.moran@mahouse.gov">john.moran@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJM1.jpg" alt="Michael , Moran">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJM1">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MJM1">Moran</a></td>
                                    <td>18th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>343</td>
                                    <td>(617) 722-2300</td>
                                    <td>                                            <a href="mailto:Michael.Moran@mahouse.gov">Michael.Moran@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DKM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DKM1.jpg" alt="David , Muradian">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DKM1">David</a></td>
                                        <td><a href="/Legislators/Profile/DKM1">Muradian</a></td>
                                    <td>9th Worcester</td>
                                    <td>Republican</td>
                                    <td>128</td>
                                    <td>(617) 722-2240</td>
                                    <td>                                            <a href="mailto:David.Muradian@mahouse.gov">David.Muradian@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JMM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JMM1.jpg" alt="James , Murphy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JMM1">James</a></td>
                                        <td><a href="/Legislators/Profile/JMM1">Murphy</a></td>
                                    <td>4th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>254</td>
                                    <td>(617) 722-2220</td>
                                    <td>                                            <a href="mailto:James.Murphy@mahouse.gov">James.Murphy@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BWM1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BWM1.jpg" alt="Brian , Murray">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BWM1">Brian</a></td>
                                        <td><a href="/Legislators/Profile/BWM1">Murray</a></td>
                                    <td>10th Worcester</td>
                                    <td>Democrat</td>
                                    <td>238</td>
                                    <td>(617) 722-2400</td>
                                    <td>                                            <a href="mailto:Brian.Murray@mahouse.gov">Brian.Murray@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TTN1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TTN1.jpg" alt="Tram , Nguyen">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TTN1">Tram</a></td>
                                        <td><a href="/Legislators/Profile/TTN1">Nguyen</a></td>
                                    <td>18th Essex</td>
                                    <td>Democrat</td>
                                    <td>36</td>
                                    <td>(617) 722-2370</td>
                                    <td>                                            <a href="mailto:tram.nguyen@mahouse.gov">tram.nguyen@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JJO1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JJO1.jpg" alt="James , O'Day">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JJO1">James</a></td>
                                        <td><a href="/Legislators/Profile/JJO1">O'Day</a></td>
                                    <td>14th Worcester</td>
                                    <td>Democrat</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:James.O'Day@mahouse.gov">James.O'Day@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/NJO1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/NJO1.jpg" alt="Norman , Orrall">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/NJO1">Norman</a></td>
                                        <td><a href="/Legislators/Profile/NJO1">Orrall</a></td>
                                    <td>12th Bristol</td>
                                    <td>Republican</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:norman.orrall@mahouse.gov">norman.orrall@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SJO1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SJO1.jpg" alt="Steven , Ouellette">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SJO1">Steven</a></td>
                                        <td><a href="/Legislators/Profile/SJO1">Ouellette</a></td>
                                    <td>8th Bristol</td>
                                    <td>Democrat</td>
                                    <td>B1</td>
                                    <td>(617) 722-2800 x7303</td>
                                    <td>                                            <a href="mailto:Steve.Ouellette@mahouse.gov">Steve.Ouellette@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SCO1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SCO1.jpg" alt="Steven , Owens">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SCO1">Steven</a></td>
                                        <td><a href="/Legislators/Profile/SCO1">Owens</a></td>
                                    <td>29th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>446</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Steven.Owens@mahouse.gov">Steven.Owens@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/FEP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/FEP1.jpg" alt="Francisco , Paulino">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/FEP1">Francisco</a></td>
                                        <td><a href="/Legislators/Profile/FEP1">Paulino</a></td>
                                    <td>16th Essex</td>
                                    <td>Democrat</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:Francisco.Paulino@mahouse.gov">Francisco.Paulino@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KWP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KWP1.jpg" alt="Kelly , Pease">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KWP1">Kelly</a></td>
                                        <td><a href="/Legislators/Profile/KWP1">Pease</a></td>
                                    <td>4th Hampden</td>
                                    <td>Republican</td>
                                    <td>237</td>
                                    <td>(413) 875-8787</td>
                                    <td>                                            <a href="mailto:Kelly.Pease@mahouse.gov">Kelly.Pease@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AHP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AHP1.jpg" alt="Alice , Peisch">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AHP1">Alice</a></td>
                                        <td><a href="/Legislators/Profile/AHP1">Peisch</a></td>
                                    <td>14th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>234</td>
                                    <td>(617) 722-2783</td>
                                    <td>                                            <a href="mailto:Alice.Peisch@mahouse.gov">Alice.Peisch@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/ERP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/ERP1.jpg" alt="Edward , Philips">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/ERP1">Edward</a></td>
                                        <td><a href="/Legislators/Profile/ERP1">Philips</a></td>
                                    <td>8th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>134</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Edward.Philips@mahouse.gov">Edward.Philips@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BMP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BMP1.jpg" alt="Bridget , Plouffe">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BMP1">Bridget</a></td>
                                        <td><a href="/Legislators/Profile/BMP1">Plouffe</a></td>
                                    <td>9th Plymouth</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7315</td>
                                    <td>                                            <a href="mailto:Bridget.Plouffe@mahouse.gov">Bridget.Plouffe@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AJP1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AJP1.jpg" alt="Angelo , Puppolo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AJP1">Angelo</a></td>
                                        <td><a href="/Legislators/Profile/AJP1">Puppolo</a></td>
                                    <td>12th Hampden</td>
                                    <td>Democrat</td>
                                    <td>122</td>
                                    <td>(617) 722-2006</td>
                                    <td>                                            <a href="mailto:Angelo.Puppolo@mahouse.gov">Angelo.Puppolo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/APR1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/APR1.jpg" alt="Adrianne , Ramos">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/APR1">Adrianne</a></td>
                                        <td><a href="/Legislators/Profile/APR1">Ramos</a></td>
                                    <td>14th Essex</td>
                                    <td>Democrat</td>
                                    <td>21</td>
                                    <td>(617) 722-2140</td>
                                    <td>                                            <a href="mailto:Adrianne.Ramos@mahouse.gov">Adrianne.Ramos@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/O_R1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/O_R1.jpg" alt="Orlando , Ramos">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/O_R1">Orlando</a></td>
                                        <td><a href="/Legislators/Profile/O_R1">Ramos</a></td>
                                    <td>9th Hampden</td>
                                    <td>Democrat</td>
                                    <td>236</td>
                                    <td>(617) 722-2430</td>
                                    <td>                                            <a href="mailto:Orlando.Ramos@mahouse.gov">Orlando.Ramos@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/S_R1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/S_R1.jpg" alt="Sean , Reid">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/S_R1">Sean</a></td>
                                        <td><a href="/Legislators/Profile/S_R1">Reid</a></td>
                                    <td>11th Essex</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7316</td>
                                    <td>                                            <a href="mailto:Sean.Reid@mahouse.gov">Sean.Reid@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/EAR1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/EAR1.jpg" alt="Estela , Reyes">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/EAR1">Estela</a></td>
                                        <td><a href="/Legislators/Profile/EAR1">Reyes</a></td>
                                    <td>4th Essex</td>
                                    <td>Democrat</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:Estela.Reyes@mahouse.gov">Estela.Reyes@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/D_R1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/D_R1.jpg" alt="David , Robertson">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/D_R1">David</a></td>
                                        <td><a href="/Legislators/Profile/D_R1">Robertson</a></td>
                                    <td>19th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473F</td>
                                    <td>(617) 722-2210</td>
                                    <td>                                            <a href="mailto:david.robertson@mahouse.gov">david.robertson@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DMR1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DMR1.jpg" alt="David , Rogers">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DMR1">David</a></td>
                                        <td><a href="/Legislators/Profile/DMR1">Rogers</a></td>
                                    <td>24th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473B</td>
                                    <td>(617) 722-2263</td>
                                    <td>                                            <a href="mailto:Dave.Rogers@mahouse.gov">Dave.Rogers@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JHR1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JHR1.jpg" alt="John , Rogers">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JHR1">John</a></td>
                                        <td><a href="/Legislators/Profile/JHR1">Rogers</a></td>
                                    <td>12th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>155</td>
                                    <td>(617) 722-2450</td>
                                    <td>                                            <a href="mailto:John.Rogers@mahouse.gov">John.Rogers@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JNR1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JNR1.jpg" alt="Jeffrey , Roy">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JNR1">Jeffrey</a></td>
                                        <td><a href="/Legislators/Profile/JNR1">Roy</a></td>
                                    <td>10th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>7</td>
                                    <td>(617) 722-2040</td>
                                    <td>                                            <a href="mailto:Jeffrey.Roy@mahouse.gov">Jeffrey.Roy@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/djr1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/djr1.jpg" alt="Daniel , Ryan">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/djr1">Daniel</a></td>
                                        <td><a href="/Legislators/Profile/djr1">Ryan</a></td>
                                    <td>2nd Suffolk</td>
                                    <td>Democrat</td>
                                    <td>156</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Dan.Ryan@mahouse.gov">Dan.Ryan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/L_S1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/L_S1.jpg" alt="Lindsay , Sabadosa">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/L_S1">Lindsay</a></td>
                                        <td><a href="/Legislators/Profile/L_S1">Sabadosa</a></td>
                                    <td>1st Hampshire</td>
                                    <td>Democrat</td>
                                    <td>160</td>
                                    <td>(617) 722-2304</td>
                                    <td>                                            <a href="mailto:lindsay.sabadosa@mahouse.gov">lindsay.sabadosa@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AMS3">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AMS3.jpg" alt="Amy , Sangiolo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AMS3">Amy</a></td>
                                        <td><a href="/Legislators/Profile/AMS3">Sangiolo</a></td>
                                    <td>11th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7317</td>
                                    <td>                                            <a href="mailto:Amy.Sangiolo@mahouse.gov">Amy.Sangiolo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/ALS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/ALS1.jpg" alt="Aaron , Saunders">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/ALS1">Aaron</a></td>
                                        <td><a href="/Legislators/Profile/ALS1">Saunders</a></td>
                                    <td>7th Hampden</td>
                                    <td>Democrat</td>
                                    <td>34</td>
                                    <td>(617) 722-2320</td>
                                    <td>                                            <a href="mailto:Aaron.Saunders@mahouse.gov">Aaron.Saunders@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AJS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AJS1.jpg" alt="Adam , Scanlon">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AJS1">Adam</a></td>
                                        <td><a href="/Legislators/Profile/AJS1">Scanlon</a></td>
                                    <td>14th Bristol</td>
                                    <td>Democrat</td>
                                    <td>127</td>
                                    <td>(617) 722-2680</td>
                                    <td>                                            <a href="mailto:Adam.Scanlon@mahouse.gov">Adam.Scanlon@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MRS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MRS1.jpg" alt="Margaret , Scarsdale">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MRS1">Margaret</a></td>
                                        <td><a href="/Legislators/Profile/MRS1">Scarsdale</a></td>
                                    <td>1st Middlesex</td>
                                    <td>Democrat</td>
                                    <td>130</td>
                                    <td>(617) 722-2130</td>
                                    <td>                                            <a href="mailto:Margaret.Scarsdale@mahouse.gov">Margaret.Scarsdale@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/G_S1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/G_S1.jpg" alt="Greg , Schwartz">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/G_S1">Greg</a></td>
                                        <td><a href="/Legislators/Profile/G_S1">Schwartz</a></td>
                                    <td>12th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7318</td>
                                    <td>                                            <a href="mailto:Greg.Schwartz@mahouse.gov">Greg.Schwartz@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DAS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DAS1.jpg" alt="Danillo , Sena">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DAS1">Danillo</a></td>
                                        <td><a href="/Legislators/Profile/DAS1">Sena</a></td>
                                    <td>37th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>39</td>
                                    <td>(617) 722-2014</td>
                                    <td>                                            <a href="mailto:Danillo.Sena@mahouse.gov">Danillo.Sena@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/D_S1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/D_S1.jpg" alt="Dawne , Shand">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/D_S1">Dawne</a></td>
                                        <td><a href="/Legislators/Profile/D_S1">Shand</a></td>
                                    <td>1st Essex</td>
                                    <td>Democrat</td>
                                    <td>134</td>
                                    <td>(617) 722-2400</td>
                                    <td>                                            <a href="mailto:Dawne.Shand@mahouse.gov">Dawne.Shand@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/A_S1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/A_S1.jpg" alt="Alan , Silvia">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/A_S1">Alan</a></td>
                                        <td><a href="/Legislators/Profile/A_S1">Silvia</a></td>
                                    <td>7th Bristol</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2230</td>
                                    <td>                                            <a href="mailto:Alan.Silvia@mahouse.gov">Alan.Silvia@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TMS2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TMS2.jpg" alt="Todd , Smola">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TMS2">Todd</a></td>
                                        <td><a href="/Legislators/Profile/TMS2">Smola</a></td>
                                    <td>1st Hampden</td>
                                    <td>Republican</td>
                                    <td>124</td>
                                    <td>(617) 722-2100</td>
                                    <td>                                            <a href="mailto:Todd.Smola@mahouse.gov">Todd.Smola@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MJS3">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MJS3.jpg" alt="Michael , Soter">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MJS3">Michael</a></td>
                                        <td><a href="/Legislators/Profile/MJS3">Soter</a></td>
                                    <td>8th Worcester</td>
                                    <td>Republican</td>
                                    <td>550</td>
                                    <td>(617) 722-2305</td>
                                    <td>                                            <a href="mailto:michael.soter@mahouse.gov">michael.soter@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/PSS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/PSS1.jpg" alt="Priscila , Sousa">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/PSS1">Priscila</a></td>
                                        <td><a href="/Legislators/Profile/PSS1">Sousa</a></td>
                                    <td>6th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>443</td>
                                    <td>(617) 722-2460</td>
                                    <td>                                            <a href="mailto:Priscila.Sousa@mahouse.gov">Priscila.Sousa@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TMS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TMS1.jpg" alt="Thomas , Stanley">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TMS1">Thomas</a></td>
                                        <td><a href="/Legislators/Profile/TMS1">Stanley</a></td>
                                    <td>9th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>167</td>
                                    <td>(617) 722-2810</td>
                                    <td>                                            <a href="mailto:Thomas.Stanley@mahouse.gov">Thomas.Stanley@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AMS2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AMS2.jpg" alt="Alyson , Sullivan-Almeida">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AMS2">Alyson</a></td>
                                        <td><a href="/Legislators/Profile/AMS2">Sullivan-Almeida</a></td>
                                    <td>7th Plymouth</td>
                                    <td>Republican</td>
                                    <td>548</td>
                                    <td>(617) 722-2488</td>
                                    <td>                                            <a href="mailto:alyson.sullivan@mahouse.gov">alyson.sullivan@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/KPS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/KPS1.jpg" alt="Kenneth , Sweezey">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/KPS1">Kenneth</a></td>
                                        <td><a href="/Legislators/Profile/KPS1">Sweezey</a></td>
                                    <td>6th Plymouth</td>
                                    <td>Republican</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7319</td>
                                    <td>                                            <a href="mailto:Ken.Sweezey@mahouse.gov">Ken.Sweezey@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MDS1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MDS1.jpg" alt="Mark , Sylvia">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MDS1">Mark</a></td>
                                        <td><a href="/Legislators/Profile/MDS1">Sylvia</a></td>
                                    <td>10th Bristol</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7320</td>
                                    <td>                                            <a href="mailto:Mark.Sylvia@mahouse.gov">Mark.Sylvia@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/J_T1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_T1.jpg" alt="Joshua , Tarsky">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_T1">Joshua</a></td>
                                        <td><a href="/Legislators/Profile/J_T1">Tarsky</a></td>
                                    <td>13th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7322</td>
                                    <td>                                            <a href="mailto:Joshua.Tarsky@mahouse.gov">Joshua.Tarsky@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/J_T2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/J_T2.jpg" alt="Justin , Thurber">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/J_T2">Justin</a></td>
                                        <td><a href="/Legislators/Profile/J_T2">Thurber</a></td>
                                    <td>5th Bristol</td>
                                    <td>Republican</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7314</td>
                                    <td>                                            <a href="mailto:Justin.Thurber@mahouse.gov">Justin.Thurber@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JRT1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JRT1.jpg" alt="Jeffrey , Turco">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JRT1">Jeffrey</a></td>
                                        <td><a href="/Legislators/Profile/JRT1">Turco</a></td>
                                    <td>19th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>473B</td>
                                    <td>(617) 722-2263</td>
                                    <td>                                            <a href="mailto:Jeffrey.Turco@mahouse.gov">Jeffrey.Turco@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/C_T1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/C_T1.jpg" alt="Chynah , Tyler">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/C_T1">Chynah</a></td>
                                        <td><a href="/Legislators/Profile/C_T1">Tyler</a></td>
                                    <td>7th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>33</td>
                                    <td>(617) 722-2060</td>
                                    <td>                                            <a href="mailto:Chynah.Tyler@mahouse.gov">Chynah.Tyler@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/S_G2">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/S_G2.jpg" alt="Steven , Ultrino">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/S_G2">Steven</a></td>
                                        <td><a href="/Legislators/Profile/S_G2">Ultrino</a></td>
                                    <td>33rd Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473G</td>
                                    <td>(617) 722-2070</td>
                                    <td>                                            <a href="mailto:Steven.Ultrino@mahouse.gov">Steven.Ultrino@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/E_U1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/E_U1.jpg" alt="Erika , Uyterhoeven">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/E_U1">Erika</a></td>
                                        <td><a href="/Legislators/Profile/E_U1">Uyterhoeven</a></td>
                                    <td>27th Middlesex</td>
                                    <td>Democrat</td>
                                    <td>473B</td>
                                    <td>(508) 319-9510</td>
                                    <td>                                            <a href="mailto:Erika.Uyterhoeven@mahouse.gov">Erika.Uyterhoeven@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/AXV1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/AXV1.jpg" alt="Andres , Vargas">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/AXV1">Andres</a></td>
                                        <td><a href="/Legislators/Profile/AXV1">Vargas</a></td>
                                    <td>3rd Essex</td>
                                    <td>Democrat</td>
                                    <td>26</td>
                                    <td>(617) 722-2080</td>
                                    <td>                                            <a href="mailto:andy.vargas@mahouse.gov">andy.vargas@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/MSV1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/MSV1.jpg" alt="Marcus , Vaughn">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/MSV1">Marcus</a></td>
                                        <td><a href="/Legislators/Profile/MSV1">Vaughn</a></td>
                                    <td>9th Norfolk</td>
                                    <td>Republican</td>
                                    <td>473B</td>
                                    <td>(617) 722-2263</td>
                                    <td>                                            <a href="mailto:Marcus.Vaughn@mahouse.gov">Marcus.Vaughn@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DTV1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DTV1.jpg" alt="David , Vieira">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DTV1">David</a></td>
                                        <td><a href="/Legislators/Profile/DTV1">Vieira</a></td>
                                    <td>3rd Barnstable</td>
                                    <td>Republican</td>
                                    <td>167</td>
                                    <td>(617) 722-2230</td>
                                    <td>                                            <a href="mailto:David.Vieira@mahouse.gov">David.Vieira@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/T_V1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/T_V1.jpg" alt="Tommy , Vitolo">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/T_V1">Tommy</a></td>
                                        <td><a href="/Legislators/Profile/T_V1">Vitolo</a></td>
                                    <td>15th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>254</td>
                                    <td>(617) 722-2220</td>
                                    <td>                                            <a href="mailto:tommy.vitolo@mahouse.gov">tommy.vitolo@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/TJW1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/TJW1.jpg" alt="Thomas , Walsh">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/TJW1">Thomas</a></td>
                                        <td><a href="/Legislators/Profile/TJW1">Walsh</a></td>
                                    <td>12th Essex</td>
                                    <td>Democrat</td>
                                    <td>20</td>
                                    <td>(617) 722-2410</td>
                                    <td>                                            <a href="mailto:Thomas.Walsh@mahouse.gov">Thomas.Walsh@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/RGW1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/RGW1.jpg" alt="Richard , Wells">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/RGW1">Richard</a></td>
                                        <td><a href="/Legislators/Profile/RGW1">Wells</a></td>
                                    <td>7th Norfolk</td>
                                    <td>Democrat</td>
                                    <td>B2</td>
                                    <td>(617) 722-2800 x7301</td>
                                    <td>                                            <a href="mailto:Richard.Wells@mahouse.gov">Richard.Wells@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SLG1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SLG1.jpg" alt="Susannah , Whipps">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SLG1">Susannah</a></td>
                                        <td><a href="/Legislators/Profile/SLG1">Whipps</a></td>
                                    <td>2nd Franklin</td>
                                    <td>Unenrolled</td>
                                    <td>540</td>
                                    <td>(617) 722-2090</td>
                                    <td>                                            <a href="mailto:Susannah.Whipps@mahouse.gov">Susannah.Whipps@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/BLW1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/BLW1.jpg" alt="Bud , Williams">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/BLW1">Bud</a></td>
                                        <td><a href="/Legislators/Profile/BLW1">Williams</a></td>
                                    <td>11th Hampden</td>
                                    <td>Democrat</td>
                                    <td>236</td>
                                    <td>(617) 722-2430</td>
                                    <td>                                            <a href="mailto:Bud.Williams@mahouse.gov">Bud.Williams@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/DHW1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/DHW1.jpg" alt="Donald , Wong">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/DHW1">Donald</a></td>
                                        <td><a href="/Legislators/Profile/DHW1">Wong</a></td>
                                    <td>9th Essex</td>
                                    <td>Republican</td>
                                    <td>541</td>
                                    <td>(617) 722-2488</td>
                                    <td>                                            <a href="mailto:Donald.Wong@mahouse.gov">Donald.Wong@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/CJW1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/CJW1.jpg" alt="Christopher , Worrell">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/CJW1">Christopher</a></td>
                                        <td><a href="/Legislators/Profile/CJW1">Worrell</a></td>
                                    <td>5th Suffolk</td>
                                    <td>Democrat</td>
                                    <td>136</td>
                                    <td>(617) 722-2396</td>
                                    <td>                                            <a href="mailto:Christopher.Worrell@mahouse.gov">Christopher.Worrell@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/SGX1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/SGX1.jpg" alt="Steven , Xiarhos">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/SGX1">Steven</a></td>
                                        <td><a href="/Legislators/Profile/SGX1">Xiarhos</a></td>
                                    <td>5th Barnstable</td>
                                    <td>Republican</td>
                                    <td>542</td>
                                    <td>(617) 722-2488</td>
                                    <td>                                            <a href="mailto:Steven.Xiarhos@mahouse.gov">Steven.Xiarhos@mahouse.gov</a>
</td>
                                </tr>
                                <tr>
                                    <td class="text-center">
        <a data-target="#exclusiveFeatureModal" data-toggle="modal" aria-pressed="false" title="Follow in MyLegislature" aria-haspopup="true" tabindex="0">
            <span class="fa fa-star fa-fw mlNotFollowing"></span>
        </a>
                                    </td>
                                        <td class="pictureCol">
                                            <a href="/Legislators/Profile/JDZ1">
                                                <div class="thumb">
                                                    <img src="/Legislators/Profile/70/JDZ1.jpg" alt="Jonathan , Zlotnik">
                                                </div>
                                            </a>
                                        </td>
                                        <td><a href="/Legislators/Profile/JDZ1">Jonathan</a></td>
                                        <td><a href="/Legislators/Profile/JDZ1">Zlotnik</a></td>
                                    <td>2nd Worcester</td>
                                    <td>Democrat</td>
                                    <td>449</td>
                                    <td>(617) 722-2582</td>
                                    <td>                                            <a href="mailto:Jon.Zlotnik@mahouse.gov">Jon.Zlotnik@mahouse.gov</a>
</td>
                                </tr>
                                                            <tr>
                                    <td class="text-center">
                                        <span class="vacantStarPlaceholder" aria-hidden="true"></span>
                                    </td>
                                    <td class="pictureCol">
                                        <a href="/Legislators/District/3rdBristol">
                                            <div class="thumb">
                                                <img src="/Legislators/Profile/NoPhotoAvailable.jpg?Name=3rd%20Bristol&amp;width=70" alt="Vacant , 3rd Bristol">
                                            </div>
                                        </a>
                                    </td>
                                    <td><a href="/Legislators/District/3rdBristol">Vacant</a></td>
                                    <td><a href="/Legislators/District/3rdBristol">3rd Bristol</a></td>
                                    <td></td>
                                    <td></td>
                                    <td>39</td>
                                    <td>(617) 722-2014</td>
                                    <td></td>
                                </tr>
                                <tr>
                                    <td class="text-center">
                                        <span class="vacantStarPlaceholder" aria-hidden="true"></span>
                                    </td>
                                    <td class="pictureCol">
                                        <a href="/Legislators/District/6thEssex">
                                            <div class="thumb">
                                                <img src="/Legislators/Profile/NoPhotoAvailable.jpg?Name=6th%20Essex&amp;width=70" alt="Vacant , 6th Essex">
                                            </div>
                                        </a>
                                    </td>
                                    <td><a href="/Legislators/District/6thEssex">Vacant</a></td>
                                    <td><a href="/Legislators/District/6thEssex">6th Essex</a></td>
                                    <td></td>
                                    <td></td>
                                    <td>42</td>
                                    <td>(617) 722-2370</td>
                                    <td></td>
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

with open('house.json', 'w') as json_file:
    json_file.write(json_data)

print(json_data)