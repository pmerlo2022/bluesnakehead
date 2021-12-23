# DC1-POD2-LEAF9B
# Table of Contents
<!-- toc -->

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.34.18/24 | 10.6.1.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.34.18/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |


### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC1 DC1_POD2 DC1-POD2-LEAF9B | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD2 DC1-POD2-LEAF9B
```

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| RACK9_MLAG | Vlan4094 | 172.20.2.32 | Port-Channel151 |

Dual primary detection is enabled. The detection delay is 5 seconds.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id RACK9_MLAG
   local-interface Vlan4094
   peer-address 172.20.2.32
   peer-address heartbeat 10.6.34.18 vrf mgmt
   peer-link Port-Channel151
   dual-primary detection delay 5 action errdisable all-interfaces
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **rstp**

### Global Spanning-Tree Settings

Global RSTP priority: 4096
Spanning Tree disabled for VLANs: **4094**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode rstp
no spanning-tree vlan-id 4094
spanning-tree priority 4096
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 4024 | MLAG_iBGP_Cust_A_VRF | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |
| 5024 | MLAG_iBGP_Cust_B_VRF | LEAF_PEER_L3 |

## VLANs Device Configuration

```eos
!
vlan 4024
   name MLAG_iBGP_Cust_A_VRF
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
!
vlan 5024
   name MLAG_iBGP_Cust_B_VRF
   trunk group LEAF_PEER_L3
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet15/1 | MLAG_PEER_DC1-POD2-LEAF9A_Ethernet15/1 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 151 |
| Ethernet16/1 | MLAG_PEER_DC1-POD2-LEAF9A_Ethernet16/1 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 151 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet29/1 | P2P_LINK_TO_DC1-POD2-SPINE1_Ethernet18/1 | routed | - | 172.17.2.137/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet18/1 | routed | - | 172.17.2.139/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_DC1-POD2-SPINE3_Ethernet18/1 | routed | - | 172.17.2.141/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_DC1-POD2-SPINE4_Ethernet18/1 | routed | - | 172.17.2.143/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet15/1
   description MLAG_PEER_DC1-POD2-LEAF9A_Ethernet15/1
   no shutdown
   channel-group 151 mode active
!
interface Ethernet16/1
   description MLAG_PEER_DC1-POD2-LEAF9A_Ethernet16/1
   no shutdown
   channel-group 151 mode active
!
interface Ethernet29/1
   description P2P_LINK_TO_DC1-POD2-SPINE1_Ethernet18/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.137/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet18/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.139/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_DC1-POD2-SPINE3_Ethernet18/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.141/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_DC1-POD2-SPINE4_Ethernet18/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.143/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel151 | MLAG_PEER_DC1-POD2-LEAF9A_Po151 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel151
   description MLAG_PEER_DC1-POD2-LEAF9A_Po151
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.2.20/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.5.2.19/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.2.20/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.5.2.19/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4024 |  MLAG_PEER_L3_iBGP: vrf Cust_A_VRF  |  Cust_A_VRF  |  9214  |  false  |
| Vlan4094 |  MLAG_PEER  |  default  |  9214  |  false  |
| Vlan5024 |  MLAG_PEER_L3_iBGP: vrf Cust_B_VRF  |  Cust_B_VRF  |  9214  |  false  |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan4024 |  Cust_A_VRF  |  172.20.2.33/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  172.20.2.33/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan5024 |  Cust_B_VRF  |  172.20.2.33/31  |  -  |  -  |  -  |  -  |  -  |


### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4024
   description MLAG_PEER_L3_iBGP: vrf Cust_A_VRF
   no shutdown
   mtu 9214
   vrf Cust_A_VRF
   ip address 172.20.2.33/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 9214
   no autostate
   ip address 172.20.2.33/31
!
interface Vlan5024
   description MLAG_PEER_L3_iBGP: vrf Cust_B_VRF
   no shutdown
   mtu 9214
   vrf Cust_B_VRF
   ip address 172.20.2.33/31
```

## VXLAN Interface

### VXLAN Interface Summary

#### Source Interface: Loopback1

#### UDP port: 4789

#### EVPN MLAG Shared Router MAC : mlag-system-id

#### VRF to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| Cust_A_VRF | 1025 |
| Cust_B_VRF | 2025 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-POD2-LEAF9B_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vrf Cust_A_VRF vni 1025
   vxlan vrf Cust_B_VRF vni 2025
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true|| Cust_A_VRF | true |
| Cust_B_VRF | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Cust_A_VRF
ip routing vrf Cust_B_VRF
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || Cust_A_VRF | false |
| Cust_B_VRF | false |
| mgmt | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.1.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65112.900|  10.4.2.20 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 16 ecmp 16 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65112.900 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 10.4.2.3 | 65112.100 | default | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS |
| 10.4.2.4 | 65112.100 | default | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS |
| 172.17.2.136 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.138 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.140 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.142 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.20.2.32 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER |
| 172.20.2.32 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Cust_A_VRF | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER |
| 172.20.2.32 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Cust_B_VRF | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER |

### Router BGP EVPN Address Family

- VPN import pruning is __enabled__

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Cust_A_VRF | 10.4.2.20:1025 | connected |
| Cust_B_VRF | 10.4.2.20:2025 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65112.900
   router-id 10.4.2.20
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 5
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65112.900
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 10.4.2.3 peer group EVPN-OVERLAY-PEERS
   neighbor 10.4.2.3 remote-as 65112.100
   neighbor 10.4.2.3 description DC1-POD2-LEAF1A
   neighbor 10.4.2.3 route-map RM-EVPN-FILTER-AS65112.100 out
   neighbor 10.4.2.4 peer group EVPN-OVERLAY-PEERS
   neighbor 10.4.2.4 remote-as 65112.100
   neighbor 10.4.2.4 description DC1-POD2-LEAF1B
   neighbor 10.4.2.4 route-map RM-EVPN-FILTER-AS65112.100 out
   neighbor 172.17.2.136 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.136 remote-as 65001.200
   neighbor 172.17.2.136 description DC1-POD2-SPINE1_Ethernet18/1
   neighbor 172.17.2.138 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.138 remote-as 65001.200
   neighbor 172.17.2.138 description DC1-POD2-SPINE2_Ethernet18/1
   neighbor 172.17.2.140 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.140 remote-as 65001.200
   neighbor 172.17.2.140 description DC1-POD2-SPINE3_Ethernet18/1
   neighbor 172.17.2.142 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.142 remote-as 65001.200
   neighbor 172.17.2.142 description DC1-POD2-SPINE4_Ethernet18/1
   neighbor 172.20.2.32 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.20.2.32 description DC1-POD2-LEAF9A
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      route import match-failure action discard
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target only
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Cust_A_VRF
      rd 10.4.2.20:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 10.4.2.20
      neighbor 172.20.2.32 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Cust_B_VRF
      rd 10.4.2.20:2025
      route-target import evpn 2025:2025
      route-target export evpn 2025:2025
      router-id 10.4.2.20
      neighbor 172.20.2.32 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

IGMP snooping is globally enabled.


### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.2.0/24 eq 32 |
| 20 | permit 10.5.2.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.2.0/24 eq 32
   seq 20 permit 10.5.2.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

#### RM-EVPN-FILTER-AS65112.100

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65112.100 |

#### RM-MLAG-PEER-IN

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | set origin incomplete |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-EVPN-FILTER-AS65112.100 deny 10
   match as 65112.100
!
route-map RM-EVPN-FILTER-AS65112.100 permit 20
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Cust_A_VRF | enabled |
| Cust_B_VRF | enabled |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance Cust_A_VRF
!
vrf instance Cust_B_VRF
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
