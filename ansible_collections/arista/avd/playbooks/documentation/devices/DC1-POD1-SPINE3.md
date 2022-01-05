# DC1-POD1-SPINE3
# Table of Contents
<!-- toc -->

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
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
| Management0 | oob_management | oob | mgmt | 10.6.1.12/24 | 10.6.1.1 |

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
   ip address 10.6.1.12/24
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
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE3 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE3
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

### Global Spanning-Tree Settings


## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/1 | routed | - | 172.17.0.156/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/1 | routed | - | 172.17.0.164/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/1 | routed | - | 172.17.0.172/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/1 | routed | - | 172.17.0.180/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/1 | routed | - | 172.17.0.188/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/1 | routed | - | 172.17.0.196/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/1 | routed | - | 172.17.0.204/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/1 | routed | - | 172.17.0.212/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/1 | routed | - | 172.17.0.220/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/1 | routed | - | 172.17.0.228/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/1 | routed | - | 172.17.0.236/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/1 | routed | - | 172.17.0.244/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/1 | routed | - | 172.17.0.252/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/1 | routed | - | 172.17.1.4/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/1 | routed | - | 172.17.1.12/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/1 | routed | - | 172.17.1.20/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/1 | routed | - | 172.17.1.28/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/1 | routed | - | 172.17.1.36/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/1 | routed | - | 172.17.1.44/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/1 | routed | - | 172.17.1.52/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/1 | routed | - | 172.17.1.60/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/1 | routed | - | 172.17.1.68/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/1 | routed | - | 172.17.1.76/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/1 | routed | - | 172.17.1.84/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/1 | routed | - | 172.17.1.92/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/1 | routed | - | 172.17.1.100/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/1 | routed | - | 172.17.1.108/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/1 | routed | - | 172.17.1.116/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet3/1 | routed | - | 172.16.0.23/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet3/1 | routed | - | 172.16.0.31/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet3/1 | routed | - | 172.16.0.39/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet3/1 | routed | - | 172.16.0.47/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.156/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.172/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.180/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.188/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.212/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.220/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.228/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.236/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.244/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.0.252/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.4/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.20/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.28/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.36/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.44/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.52/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.60/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.76/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.84/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.92/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.108/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.116/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.23/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.31/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.39/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.47/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.0.12/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.0.12/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true|| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || mgmt | false |


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
| 64603|  10.4.0.12 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 16 ecmp 16 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.16.0.22 | 64501 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.0.30 | 64502 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.0.38 | 64503 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.0.46 | 64504 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.157 | 64901 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.165 | 64901 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.173 | 64902 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.181 | 64902 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.189 | 64903 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.197 | 64903 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.205 | 64904 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.213 | 64904 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.221 | 64905 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.229 | 64905 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.237 | 64906 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.245 | 64906 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.0.253 | 64907 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.5 | 64907 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.13 | 64908 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.21 | 64908 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.29 | 64909 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.37 | 64909 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.45 | 64910 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.53 | 64910 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.61 | 64911 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.69 | 64911 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.77 | 64912 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.85 | 64912 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.93 | 64913 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.101 | 64913 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.109 | 64914 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.117 | 64914 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 64603
   router-id 10.4.0.12
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.0.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.22 remote-as 64501
   neighbor 172.16.0.22 description SUPER-SPINE1_Ethernet3/1
   neighbor 172.16.0.30 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.30 remote-as 64502
   neighbor 172.16.0.30 description SUPER-SPINE2_Ethernet3/1
   neighbor 172.16.0.38 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.38 remote-as 64503
   neighbor 172.16.0.38 description SUPER-SPINE3_Ethernet3/1
   neighbor 172.16.0.46 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.46 remote-as 64504
   neighbor 172.16.0.46 description SUPER-SPINE4_Ethernet3/1
   neighbor 172.17.0.157 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.157 remote-as 64901
   neighbor 172.17.0.157 description DC1-POD1-LEAF1A_Ethernet31/1
   neighbor 172.17.0.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.165 remote-as 64901
   neighbor 172.17.0.165 description DC1-POD1-LEAF1B_Ethernet31/1
   neighbor 172.17.0.173 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.173 remote-as 64902
   neighbor 172.17.0.173 description DC1-POD1-LEAF2A_Ethernet31/1
   neighbor 172.17.0.181 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.181 remote-as 64902
   neighbor 172.17.0.181 description DC1-POD1-LEAF2B_Ethernet31/1
   neighbor 172.17.0.189 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.189 remote-as 64903
   neighbor 172.17.0.189 description DC1-POD1-LEAF3A_Ethernet31/1
   neighbor 172.17.0.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.197 remote-as 64903
   neighbor 172.17.0.197 description DC1-POD1-LEAF3B_Ethernet31/1
   neighbor 172.17.0.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.205 remote-as 64904
   neighbor 172.17.0.205 description DC1-POD1-LEAF4A_Ethernet31/1
   neighbor 172.17.0.213 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.213 remote-as 64904
   neighbor 172.17.0.213 description DC1-POD1-LEAF4B_Ethernet31/1
   neighbor 172.17.0.221 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.221 remote-as 64905
   neighbor 172.17.0.221 description DC1-POD1-LEAF5A_Ethernet31/1
   neighbor 172.17.0.229 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.229 remote-as 64905
   neighbor 172.17.0.229 description DC1-POD1-LEAF5B_Ethernet31/1
   neighbor 172.17.0.237 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.237 remote-as 64906
   neighbor 172.17.0.237 description DC1-POD1-LEAF6A_Ethernet31/1
   neighbor 172.17.0.245 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.245 remote-as 64906
   neighbor 172.17.0.245 description DC1-POD1-LEAF6B_Ethernet31/1
   neighbor 172.17.0.253 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.0.253 remote-as 64907
   neighbor 172.17.0.253 description DC1-POD1-LEAF7A_Ethernet31/1
   neighbor 172.17.1.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.5 remote-as 64907
   neighbor 172.17.1.5 description DC1-POD1-LEAF7B_Ethernet31/1
   neighbor 172.17.1.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.13 remote-as 64908
   neighbor 172.17.1.13 description DC1-POD1-LEAF8A_Ethernet31/1
   neighbor 172.17.1.21 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.21 remote-as 64908
   neighbor 172.17.1.21 description DC1-POD1-LEAF8B_Ethernet31/1
   neighbor 172.17.1.29 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.29 remote-as 64909
   neighbor 172.17.1.29 description DC1-POD1-LEAF9A_Ethernet31/1
   neighbor 172.17.1.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.37 remote-as 64909
   neighbor 172.17.1.37 description DC1-POD1-LEAF9B_Ethernet31/1
   neighbor 172.17.1.45 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.45 remote-as 64910
   neighbor 172.17.1.45 description DC1-POD1-LEAF10A_Ethernet31/1
   neighbor 172.17.1.53 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.53 remote-as 64910
   neighbor 172.17.1.53 description DC1-POD1-LEAF10B_Ethernet31/1
   neighbor 172.17.1.61 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.61 remote-as 64911
   neighbor 172.17.1.61 description DC1-POD1-LEAF11A_Ethernet31/1
   neighbor 172.17.1.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.69 remote-as 64911
   neighbor 172.17.1.69 description DC1-POD1-LEAF11B_Ethernet31/1
   neighbor 172.17.1.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.77 remote-as 64912
   neighbor 172.17.1.77 description DC1-POD1-LEAF12A_Ethernet31/1
   neighbor 172.17.1.85 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.85 remote-as 64912
   neighbor 172.17.1.85 description DC1-POD1-LEAF12B_Ethernet31/1
   neighbor 172.17.1.93 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.93 remote-as 64913
   neighbor 172.17.1.93 description DC1-POD1-LEAF13A_Ethernet31/1
   neighbor 172.17.1.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.101 remote-as 64913
   neighbor 172.17.1.101 description DC1-POD1-LEAF13B_Ethernet31/1
   neighbor 172.17.1.109 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.109 remote-as 64914
   neighbor 172.17.1.109 description DC1-POD1-LEAF14A_Ethernet31/1
   neighbor 172.17.1.117 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.117 remote-as 64914
   neighbor 172.17.1.117 description DC1-POD1-LEAF14B_Ethernet31/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.0.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.0.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
